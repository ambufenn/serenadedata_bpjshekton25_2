import numpy as np

def ai_score(service):
    ref = float(service.get("ref_price", 0))
    price = float(service.get("unit_price", 0))
    
    if ref == 0: return 0, {"msg": "No reference price"}
    
    gap = (price - ref) / ref
    
    score = np.clip(gap, 0, 1)
    
    return float(score), {
        "service": service.get("description"),
        "ref_price": ref,
        "submitted_price": price,
        "variance_pct": round(gap*100,2)
    }
