from pydantic import BaseModel
# Importa BaseModel para definir modelos de datos y validación

from typing import Optional
# Importa Optional para campos que pueden no ser requeridos en actualizaciones parciales

class UsuarioBase(BaseModel):
    # Esquema base con los campos comunes de un usuario
    nombre: str
    email: str
    contraseña: str
    rol: str

class UsuarioCreate(UsuarioBase):
    # Esquema para crear un usuario, hereda los campos base
    pass

class UsuarioRead(UsuarioBase):
    # Esquema para leer usuario, incluye campo id
    id: int

    class Config:
        orm_mode = True
        # Permite que Pydantic trabaje con objetos ORM (SQLModel, SQLAlchemy)

class UsuarioUpdate(BaseModel):
    # Esquema para actualización parcial (PATCH), todos los campos son opcionales
    nombre: Optional[str]
    email: Optional[str]
    contraseña: Optional[str]
    rol: Optional[str]
