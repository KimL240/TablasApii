from pydantic import BaseModel
from datetime import date
from typing import Optional

class PagoBase(BaseModel):
    pedido_id: int
    monto: float
    metodo_pago: str
    fecha_pago: date

class PagoCreate(PagoBase):
    pass

class PagoRead(PagoBase):
    id: int
    class Config:
        orm_mode = True

class PagoUpdate(BaseModel):
    pedido_id: Optional[int]
    monto: Optional[float]
    metodo_pago: Optional[str]
    fecha_pago: Optional[date]
