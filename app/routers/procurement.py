from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.sql import crud

from app.database import SessionLocal
from app.models.model import CustomerPurchase, Payment, Customer, DailyExpenses
from app.schemas.customer import CustomerResponse
from app.schemas.procurement import ProcurementCreate

router = APIRouter(prefix="/procurement", tags=["procurement"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_procurement(procurement: ProcurementCreate, db: Session = Depends(get_db)):
    # ví dụ: insert DB (ở đây mock data)
    customer_id : int
    try:

        customer = db.query(Customer).filter(func.lower(Customer.customer_name) == procurement.customer_name.lower()).first()
        if not customer:
            customer = Customer(
                customer_name = procurement.customer_name,
                phone_number = procurement.customer_phone,
            )
            db.add(customer)
            db.commit()
            db.refresh(customer)
        new_transaction = CustomerPurchase(
            customer_id = customer.customer_id,
            quantity_kg = procurement.total_kg,
            unit_price = procurement.unit_price,
            total_amount = procurement.total_amount,
        )
        db.add(new_transaction)
        db.commit()
        db.refresh(new_transaction)

        voucher_no = generate_invoice_code(customer.customer_id)
        payment_method = 'Tiền mặt' if procurement.payment_methods == 0 else 'Chuyển khoản'
        new_payment = Payment(
            customer_id = customer.customer_id,
            amount = procurement.amount_paid,
            voucher_no =voucher_no,
            payment_method = payment_method,
        )
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)

        cash_type = 'TM' if procurement.payment_methods == 0 else 'CK'
        new_daily_expenses = DailyExpenses(
            category_id=7,
            amount=procurement.amount_paid,
            cash_type=cash_type,
        )
        db.add(new_daily_expenses)
        db.commit()
        db.refresh(new_daily_expenses)

        print(procurement)
        return {
            "status": "success",
            "message": "Nhập hàng thành công",
            "data": procurement
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

def generate_invoice_code(customer_id: int) -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"HDMB{customer_id}_{timestamp}"