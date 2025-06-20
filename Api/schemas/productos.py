from pydantic import BaseModel
# Importa BaseModel para definir y validar esquemas de datos

from typing import Optional
# Importa Optional para campos que pueden ser omitidos en actualizaciones parciales

class productoBase(BaseModel):
    # Esquema base con campos comunes para un producto
    nombre: str
    precio: float
    categoria_id: int

class productoCreate(productoBase):
    # Esquema para crear un producto (hereda los campos base)
    pass

class productoRead(productoBase):
    # Esquema para leer un producto, incluye el campo id
    id: int

    class config:
        orm_mode = True
        # ⚠️ Atención: hay un error tipográfico, debe ser "Config" con C mayúscula
        # Esto habilita la compatibilidad con ORM (SQLModel/SQLAlchemy)

class productoUpdate(BaseModel):
    # Esquema para actualización parcial de un producto
    nombre: Optional[str]
    precio: Optional[float]
    categoria_id: Optional[int]
    # Todos los campos opcionales para permitir modificaciones parciales
