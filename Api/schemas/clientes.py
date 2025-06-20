from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str
    usuario_id: int

class ClienteCreate(ClienteBase):
    pass

class ClienteRead(ClienteBase):
    id: int

    class Config:
        orm_mode = True

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    usuario_id: Optional[int] = None
