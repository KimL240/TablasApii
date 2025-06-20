from pydantic import BaseModel
# Importa BaseModel para definir esquemas y validar datos

from typing import Optional
# Importa Optional para campos que pueden ser omitidos en actualizaciones

class DireccionBase(BaseModel):
    # Esquema base con los campos comunes para una dirección
    ciudad: str
    pais: str
    cliente_id: int

class DireccionCreate(DireccionBase):
    # Esquema para creación de una dirección (hereda los campos base)
    pass

class DireccionRead(DireccionBase):
    # Esquema para lectura de dirección, incluye el campo id
    id: int

    class Config:
        orm_mode = True
        # Permite trabajar directamente con objetos ORM (SQLModel)

class DireccionUpdate(BaseModel):
    # Esquema para actualización parcial de dirección
    ciudad: Optional[str]
    pais: Optional[str]
    cliente_id: Optional[int]
    # Todos opcionales para permitir actualizaciones parciales (PATCH)
