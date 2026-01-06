import datetime
from decimal import Decimal

from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric


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

#Bảng mua
class Transaction(Base):
    __tablename__ = "customer_transactions"
    transaction_id = Column(Integer, primary_key=True, index=True)
    transaction_date = Column(DateTime, default=datetime.datetime.utcnow)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    invoice_no = Column(String(50), nullable=True)
    quantity = Column(Integer, nullable=True)
    unit_price = Column(Integer, nullable=True)
    total_amount = Column(Integer, nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

# trả tiền cho khách
class Payment(Base):
    __tablename__ = "customer_payments"
    payment_id = Column(Integer, primary_key=True, index=True)
    payment_date = Column(DateTime, default=datetime.datetime.utcnow)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    voucher_no = Column(String(50), nullable=True)
    paid_amount = Column(Numeric(18, 2), nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )
