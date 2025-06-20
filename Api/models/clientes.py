from sqlmodel import SQLModel, Field, Relationship
from typing import Optional,List,TYPE_CHECKING

if TYPE_CHECKING:
    from Api.models.usuario import Usuario
    from Api.models.direcciones import direcciones
    
class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    usuario_id: int = Field(foreign_key="usuario.id")
    usuario: Optional['Usuario'] =Relationship(back_populates="clientes")
    direccione: List['direcciones'] = Relationship(back_populates="clientes")