import datetime
from decimal import Decimal

from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(50), unique=True, nullable=False)
    phone_number = Column(String(50), nullable=True)
    note = Column(String(255), nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

#Bảng mua
class CustomerPurchase(Base):
    __tablename__ = "customer_purchase"

    purchase_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    purchase_date = Column(DateTime, default=datetime.datetime.utcnow)
    quantity_kg = Column(Integer, nullable=True)
    unit_price = Column(Integer, nullable=True)
    total_amount = Column(Integer, nullable=True)
    note = Column(String(255), nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

# trả tiền cho khách
class Payment(Base):
    __tablename__ = "payments"
    payment_id = Column(Integer, primary_key=True, index=True)
    payment_date = Column(DateTime, default=datetime.datetime.utcnow)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    voucher_no = Column(String(50), nullable=True)
    payment_method = Column(String(50), nullable=True)
    note = Column(String(255), nullable=True)
    amount = Column(Numeric(18, 2), nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

#bảng chi
class DailyExpenses(Base):
    __tablename__ = "daily_expenses"
    expense_id = Column(Integer, primary_key=True, index=True)
    expense_date = Column(DateTime, default=datetime.datetime.utcnow)
    category_id = Column(Integer, ForeignKey("cash_categories.category_id"))
    amount = Column(Numeric(18, 2), nullable=True)
    cash_type = Column(String(2), nullable=False)
    note = Column(String(255), nullable=True)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

class CashCategory(Base):
    __tablename__ = "cash_categories"
    category_id = Column(Integer, primary_key=True, index=True)
    category_type = Column(String(2), nullable=False)
    category_name = Column(String(100), nullable=True)