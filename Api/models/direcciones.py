from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,List
from Api.models.clientes import Cliente

class direcciones(SQLModel, Table=True):
    id: Optional[int]= Field(default=None, primary_key=True)
    cuidad: str
    pais: str
    cliente_id: int = Field(foreign_key="cliente.id")
    cliente: Optional[Cliente] = Relationship(back_populates="direcciones")