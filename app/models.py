from sqlalchemy import Column, Integer, String, DECIMAL, Date
from .database import Base

class Deal(Base):
    __tablename__ = "Deals"

    id = Column(Integer, primary_key=True, index=True)
    deal_name = Column(String(255))
    company_from = Column(String(255))
    company_to = Column(String(255))
    deal_size = Column(DECIMAL(18, 2))
    deal_type = Column(String(100))
    sector = Column(String(100))
    date_closed = Column(Date)
    lead_bank = Column(String(255))
    description = Column(String)
