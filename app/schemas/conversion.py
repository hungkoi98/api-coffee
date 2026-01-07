import datetime
from typing import Optional

from pydantic import BaseModel

class ConversionResponse(BaseModel):
    khoi_luong_vao: int
    do_am: float
    khoi_luong: float
    gia_nhan: float

    class Config:
        from_attributes = True