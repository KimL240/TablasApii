from sqlmodel import SQLModel, Field, Relationship
# Importa las clases para definir modelos, campos y relaciones en SQLModel

from typing import Optional, List, TYPE_CHECKING
# Importa herramientas para tipado: Optional para campos opcionales, List para listas tipadas,
# y TYPE_CHECKING para evitar importaciones circulares

from datetime import date
# Importa la clase date para manejar fechas

if TYPE_CHECKING:
    from Api.models.pedidos import Pedido
    # Importación condicional para evitar dependencias circulares,
    # usada solo para verificación estática de tipos

class Pago(SQLModel, table=True):
    # Define el modelo 'Pago' como tabla en la base de datos
    # Representa un pago realizado para un pedido

    id: Optional[int] = Field(default=None, primary_key=True)
    # Campo 'id' opcional que será clave primaria autogenerada

    pedido_id: int = Field(foreign_key="pedido.id")
    # Clave foránea que referencia al id del pedido asociado a este pago

    monto: float
    # Monto pagado

    metodo_pago: str
    # Método utilizado para el pago (ejemplo: tarjeta, efectivo, transferencia)

    fecha_pago: date
    # Fecha en que se realizó el pago

    pedido: Optional['Pedido'] = Relationship(back_populates="pagos")
    # Relación opcional con el modelo Pedido,
    # 'back_populates' indica que en Pedido hay un campo 'pagos' que completa la relación
