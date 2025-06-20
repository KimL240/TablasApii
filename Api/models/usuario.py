from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,List
from Api.models.clientes import Cliente

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str
    contraseña: str
    rol: str
    clientes: List["Cliente"] = Relationship(back_populates="usuario")
