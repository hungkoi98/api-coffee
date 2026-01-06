import datetime

from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(50), unique=True, nullable=False)
    phone_number = Column(Integer, nullable=False)
    note = Column(String(255), nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )