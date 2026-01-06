from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.model import Transaction, Payment, Customer
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
    customer = db.query(Customer).filter(Customer.customer_name == procurement.customer_name).first()
    if not customer:
        customer = Customer(
            customer_name = procurement.customer_name,
            phone_number = procurement.phone_number,
        )
        db.add(customer)
        db.commit()
        db.refresh(customer)
    new_transaction = Transaction(
        customer_id = customer.customer_id,
        quantity = procurement.total_kg,
        unit_price = procurement.unit_price,
        total_amount = procurement.total_amount,
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    new_payment = Payment(
        customer_id = customer.customer_id,
        paid_amount = procurement.amount_paid,
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    print(procurement)
    return {
        "status": "success",
        "message": "Nhập hàng thành công",
        "data": procurement
    }