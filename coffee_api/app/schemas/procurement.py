from typing import Optional

from pydantic import BaseModel

class ProcurementCreate(BaseModel):
    customer_name: str
    customer_phone: str
    total_kg: float
    unit_price: float
    total_amount: float
    amount_paid: float
    payment_methods: int
    customer_type: int

    class Config:
        from_attributes = True