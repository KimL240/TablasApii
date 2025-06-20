from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from Api.models.productos import Producto

class categoria(SQLModel, table=True):
    id: Optional[int]= Field(default=None, primary_key=True)
    nombre: str
    unidad: str
    productos: List[Producto]=Relationship(back_populates='categoria')