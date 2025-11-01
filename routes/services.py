from fastapi import APIRouter, Depends
from ..database import SessionLocal
from ..models import Service, AIFLAG
from ..ai_engine import ai_score

router = APIRouter(prefix="/services", tags=["services"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{visit_id}")
def get_services(visit_id: str, db=Depends(get_db)):
    return db.query(Service).filter(Service.visit_id == visit_id).all()


@router.post("/{visit_id}/scan")
def scan_visit(visit_id: str, db=Depends(get_db)):
    services = db.query(Service).filter(Service.visit_id == visit_id).all()

    flags = []
    for s in services:
        score, reason = ai_score({
            "unit_price": s.unit_price,
            "ref_price": 50000, # dummy ref
            "description": s.description
        })

        if score > 0.2:  # threshold
            flag = AIFLAG(
                visit_id=visit_id,
                category="cost_variance",
                risk_score=score,
                reason_json=reason
            )
            db.add(flag)
            flags.append(reason)

    db.commit()
    return {"flags": flags}
