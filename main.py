from fastapi import FastAPI
from .database import engine, Base
from .routes import patients, visits, services, feedback

app = FastAPI(title="KlinJKN Fairness Backend MVP")

Base.metadata.create_all(bind=engine)

app.include_router(patients.router)
app.include_router(visits.router)
app.include_router(services.router)
app.include_router(feedback.router)

@app.get("/")
def root():
    return {"msg": "KlinJKN API Running ✅"}
