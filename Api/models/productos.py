from typing import Optional, List,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from Api.models.categoria import categoria
    from Api.models.detalle_pedidos import DetallePedido
class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    precio: float
    categoria_id: int = Field(foreign_key="categoria.id")

    Categoria: Optional['categoria'] = Relationship(back_populates="productos")
    detalles: List['DetallePedido'] = Relationship(back_populates="producto")