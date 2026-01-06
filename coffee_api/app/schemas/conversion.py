import datetime
from typing import Optional

from pydantic import BaseModel

class ConversionResponse(BaseModel):
    do_nguyen: int
    do_le: int
    khoi_luong: float
    gia_nhan: float

    class Config:
        from_attributes = True