from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.model import Customer
from app.schemas.customer import CustomerResponse

router = APIRouter(prefix="/customers", tags=["customers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    return db.query(Customer).order_by(Customer.customer_name).all()