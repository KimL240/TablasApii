from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date
from Api.models.pedidos import Pedido

class Pago(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    pedido_id: int = Field(foreign_key="pedido.id")
    monto: float
    metodo_pago: str
    fecha_pago: date

    pedido: Optional[Pedido] = Relationship(back_populates="pagos")
