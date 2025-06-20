from sqlmodel import SQLModel, Field, Relationship
# Importa clases para definir modelos, campos y relaciones en SQLModel

from typing import Optional, List, TYPE_CHECKING
# Importa herramientas para tipado: Optional para campos opcionales, List para listas tipadas,
# y TYPE_CHECKING para evitar importaciones circulares

if TYPE_CHECKING:
    from Api.models.clientes import Cliente
    # Importación condicional para evitar dependencias circulares,
    # solo usada para verificación estática de tipos

class direcciones(SQLModel, Table=True):
    # Define el modelo 'direcciones' como tabla en la base de datos
    # (Nota: el parámetro debe ser `table=True` con minúscula, pero no modifico nada)

    id: Optional[int] = Field(default=None, primary_key=True)
    # Campo 'id' opcional que será clave primaria autogenerada

    cuidad: str
    # Campo obligatorio para la ciudad (nota: probablemente 'ciudad' es la palabra correcta)

    pais: str
    # Campo obligatorio para el país

    cliente_id: int = Field(foreign_key="cliente.id")
    # Campo clave foránea que referencia al campo 'id' de la tabla 'cliente'

    cliente: Optional['Cliente'] = Relationship(back_populates="direcciones")
    # Relación opcional con el modelo Cliente,
    # 'back_populates' indica que en Cliente hay un campo 'direcciones' que completa la relación
