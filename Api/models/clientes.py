from sqlmodel import SQLModel, Field, Relationship
# Importa las clases para definir modelos, campos y relaciones en SQLModel

from typing import Optional, List, TYPE_CHECKING
# Importa herramientas para tipado: Optional para campos opcionales, List para listas tipadas,
# y TYPE_CHECKING para evitar importaciones circulares

if TYPE_CHECKING:
    from Api.models.usuario import Usuario
    from Api.models.direcciones import direcciones
    # Importaciones condicionales para evitar dependencias circulares en tiempo de ejecución
    # Solo se usan para verificación estática de tipos

class Cliente(SQLModel, table=True):
    # Define el modelo 'Cliente' como tabla en la base de datos

    id: Optional[int] = Field(default=None, primary_key=True)
    # Campo 'id' opcional que será la clave primaria, se asigna automáticamente

    nombre: str
    # Campo obligatorio para el nombre del cliente

    usuario_id: int = Field(foreign_key="usuario.id")
    # Campo que es clave foránea que referencia al campo 'id' de la tabla 'usuario'

    usuario: Optional['Usuario'] = Relationship(back_populates="clientes")
    # Relación opcional con el modelo Usuario,
    # 'back_populates' indica que en Usuario hay un campo 'clientes' que completa la relación

    direccione: List['direcciones'] = Relationship(back_populates="clientes")
    # Relación uno-a-muchos con la tabla 'direcciones' (un cliente puede tener varias direcciones),
    # 'back_populates' apunta al campo 'clientes' en direcciones que completa la relación
