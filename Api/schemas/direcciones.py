from pydantic import BaseModel
from typing import Optional

class DireccionBase(BaseModel):
    ciudad: str
    pais: str
    cliente_id: int

class DireccionCreate(DireccionBase):
    pass

class DireccionRead(DireccionBase):
    id: int
    class Config:
        orm_mode = True

class DireccionUpdate(BaseModel):
    ciudad: Optional[str]
    pais: Optional[str]
    cliente_id: Optional[int]