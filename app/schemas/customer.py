import datetime
from typing import Optional

from pydantic import BaseModel

class CustomerResponse(BaseModel):
    customer_id: int
    customer_name: str
    phone_number: int
    note:  Optional[str] = ''

    class Config:
        from_attributes = True