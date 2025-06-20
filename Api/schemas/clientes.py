from pydantic import BaseModel
# Importa BaseModel de Pydantic para definir y validar estructuras de datos

from typing import Optional
# Importa Optional para permitir campos no obligatorios en actualizaciones parciales

class ClienteBase(BaseModel):
    # Esquema base que contiene los campos comunes para un cliente
    nombre: str
    usuario_id: int

class ClienteCreate(ClienteBase):
    # Esquema usado al crear un nuevo cliente (hereda los campos del esquema base)
    pass

class ClienteRead(ClienteBase):
    # Esquema usado para leer/retornar datos de cliente, incluye el ID
    id: int

    class Config:
        orm_mode = True
        # Permite que Pydantic lea datos directamente desde objetos ORM

class ClienteUpdate(BaseModel):
    # Esquema para actualización parcial (PATCH), todos los campos son opcionales
    nombre: Optional[str] = None
    usuario_id: Optional[int] = None
