from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Patient(Base):
    __tablename__ = "patients"
    pseudo_id = Column(String, primary_key=True)
    gender = Column(String)
    birth_year = Column(Integer)
    region = Column(String)


class Visit(Base):
    __tablename__ = "visits"
    visit_id = Column(String, primary_key=True)
    pseudo_id = Column(String, ForeignKey("patients.pseudo_id"))
    facility_id = Column(String)
    visit_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="open")


class Service(Base):
    __tablename__ = "services"
    service_id = Column(Integer, primary_key=True, autoincrement=True)
    visit_id = Column(String, ForeignKey("visits.visit_id"))
    code = Column(String)
    description = Column(String)
    qty = Column(Integer)
    unit_price = Column(Float)
    total_price = Column(Float)
    cbg_group = Column(String)


class AIFLAG(Base):
    __tablename__ = "ai_flags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    visit_id = Column(String)
    category = Column(String)
    risk_score = Column(Float)
    reason_json = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, autoincrement=True)
    visit_id = Column(String)
    role = Column(String) # patient / rs / bpjs
    message = Column(String)
    status = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
