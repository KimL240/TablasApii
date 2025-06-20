from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from Api.models.pedidos import Pedido
from Api.models.productos import Producto

class DetallePedido(SQLModel, table=True):
    pedido_id: int = Field(foreign_key="pedido.id", primary_key=True)
    producto_id: int = Field(foreign_key="producto.id", primary_key=True)
    cantidad: int
    precio_unitario: float

    pedido: Optional[Pedido] = Relationship(back_populates="detalles")
    producto: Optional[Producto] = Relationship(back_populates="detalles")
