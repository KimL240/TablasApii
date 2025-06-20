from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from Api.models.clientes import Cliente
from Api.models.detalle_pedidos import DetallePedido
from Api.models.pagos import Pago

class Pedido(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: date
    cliente_id: int = Field(foreign_key="cliente.id")

    cliente: Optional[Cliente] = Relationship(back_populates="pedidos")
    detalles: List[DetallePedido] = Relationship(back_populates="pedido")
    pagos: List[Pago] = Relationship(back_populates="pedido")
