from pydantic import BaseModel
from datetime import date
from typing import Optional

class PedidoBase(BaseModel):
    fecha: date
    cliente_id: int

class PedidoCreate(PedidoBase):
    pass

class PedidoRead(PedidoBase):
    id: int
    class Config:
        orm_mode = True

class PedidoUpdate(BaseModel):
    fecha: Optional[date]
    cliente_id: Optional[int]
