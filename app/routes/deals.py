from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models
from ..database import SessionLocal

router = APIRouter(prefix="/deals", tags=["Deals"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_all_deals(db: Session = Depends(get_db)):
    return db.query(models.Deal).all()
