from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import SessionLocal
from ..models import Deal

router = APIRouter(prefix="/analytics", tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    total_deals = db.query(func.count(Deal.id)).scalar()
    total_value = db.query(func.sum(Deal.deal_size)).scalar()
    biggest_deal = db.query(func.max(Deal.deal_size)).scalar()

    return {
        "total_deals": total_deals,
        "total_value": float(total_value or 0),
        "biggest_deal": float(biggest_deal or 0)
    }
