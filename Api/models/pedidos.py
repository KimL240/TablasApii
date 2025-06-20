from typing import Optional, List, TYPE_CHECKING
# Importa herramientas para tipado: Optional para campos opcionales,
# List para listas tipadas y TYPE_CHECKING para evitar importaciones circulares

from sqlmodel import SQLModel, Field, Relationship
# Importa las clases para definir modelos, campos y relaciones en SQLModel

from datetime import date
# Importa la clase date para manejar fechas

if TYPE_CHECKING:
    from Api.models.clientes import Cliente
    from Api.models.detalle_pedidos import DetallePedido
    from Api.models.pagos import Pago
    # Importaciones condicionales para evitar dependencias circulares,
    # usadas solo para verificación estática de tipos

class Pedido(SQLModel, table=True):
    # Define el modelo 'Pedido' como tabla en la base de datos
    # Representa un pedido realizado por un cliente

    id: Optional[int] = Field(default=None, primary_key=True)
    # Campo 'id' opcional que será clave primaria autogenerada

    fecha: date
    # Fecha en la que se realizó el pedido

    cliente_id: int = Field(foreign_key="cliente.id")
    # Clave foránea que referencia al id del cliente que hizo el pedido

    cliente: Optional['Cliente'] = Relationship(back_populates="pedidos")
    # Relación opcional con el modelo Cliente,
    # 'back_populates' indica que en Cliente hay un campo 'pedidos' que completa la relación

    detalles: List['DetallePedido'] = Relationship(back_populates="pedido")
    # Relación uno-a-muchos con DetallePedido,
    # un pedido puede tener varios detalles (productos, cantidades)

    pagos: List['Pago'] = Relationship(back_populates="pedido")
    # Relación uno-a-muchos con Pago,
    # un pedido puede tener varios pagos asociados
