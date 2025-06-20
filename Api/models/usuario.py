from sqlmodel import SQLModel, Field, Relationship
# Importa las clases para definir modelos, campos y relaciones en SQLModel

from typing import Optional, List, TYPE_CHECKING
# Importa herramientas para tipado: Optional para campos opcionales,
# List para listas tipadas y TYPE_CHECKING para evitar importaciones circulares

if TYPE_CHECKING:
    from Api.models.clientes import Cliente
    # Importación condicional para evitar dependencias circulares,
    # solo usada para verificación estática de tipos

class Usuario(SQLModel, table=True):
    # Define el modelo 'Usuario' como tabla en la base de datos
    # Representa a un usuario del sistema que puede estar relacionado con varios clientes

    id: Optional[int] = Field(default=None, primary_key=True)
    # Campo 'id' opcional que será clave primaria autogenerada

    nombre: str
    # Nombre del usuario

    email: str
    # Correo electrónico del usuario

    contraseña: str
    # Contraseña del usuario

    rol: str
    # Rol del usuario (por ejemplo: admin, empleado, cliente)

    clientes: List["Cliente"] = Relationship(back_populates="usuario")
    # Relación uno-a-muchos con Cliente,
    # un usuario puede estar asociado a varios clientes,
    # 'back_populates' indica que en Cliente hay un campo 'usuario' que completa la relación
