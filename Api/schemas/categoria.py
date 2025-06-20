from pydantic import BaseModel
# Importa BaseModel de Pydantic, que permite validar y estructurar los datos

from typing import Optional
# Importa Optional para campos que no son obligatorios (se usan en updates)

class categoriaBase(BaseModel):
    # Esquema base con los campos comunes para categoría
    nombre: str 
    unidad: str

class categoriaCreate(categoriaBase):
    # Esquema para crear una categoría (usa los mismos campos que el base)
    pass

class categoriaRead(categoriaBase):
    # Esquema para leer una categoría (incluye el ID)
    id: int

    class confing:
        orm_mode=True
        # Habilita compatibilidad con objetos ORM (modelo SQLModel o SQLAlchemy)
        # ⚠️ OJO: hay un error tipográfico en "confing", debería ser "Config"

class categriaUpdate(BaseModel):
    # Esquema para actualización parcial de una categoría
    nombre: Optional[str] = None
    unidad: Optional[str] = None
