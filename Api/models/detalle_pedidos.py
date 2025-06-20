from sqlmodel import SQLModel, Field, Relationship
# Importa las clases para definir modelos, campos y relaciones en SQLModel

from typing import Optional, List, TYPE_CHECKING
# Importa herramientas para tipado: Optional para campos opcionales, List para listas tipadas,
# y TYPE_CHECKING para evitar importaciones circulares

if TYPE_CHECKING:
    from Api.models.pedidos import Pedido
    from Api.models.productos import Producto
    # Importaciones condicionales para evitar dependencias circulares,
    # solo usadas para verificación estática de tipos

class DetallePedido(SQLModel, table=True):
    # Define el modelo 'DetallePedido' como tabla en la base de datos
    # Representa un detalle de un pedido, es decir, un producto y su cantidad dentro de un pedido

    pedido_id: int = Field(foreign_key="pedido.id", primary_key=True)
    # Clave primaria compuesta - referencia al id del pedido (clave foránea)

    producto_id: int = Field(foreign_key="producto.id", primary_key=True)
    # Clave primaria compuesta - referencia al id del producto (clave foránea)

    cantidad: int
    # Cantidad del producto en este detalle de pedido

    precio_unitario: float
    # Precio unitario del producto en el momento del pedido

    pedido: Optional['Pedido'] = Relationship(back_populates="detalles")
    # Relación opcional con el modelo Pedido,
    # 'back_populates' indica que en Pedido hay un campo 'detalles' que completa la relación

    producto: Optional['Producto'] = Relationship(back_populates="detalles")
    # Relación opcional con el modelo Producto,
    # 'back_populates' indica que en Producto hay un campo 'detalles' que completa la relación
