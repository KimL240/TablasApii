from pydantic import BaseModel

class DetallePedidoBase(BaseModel):
    pedido_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float

class DetallePedidoCreate(DetallePedidoBase):
    pass

class DetallePedidoRead(DetallePedidoBase):
    class Config:
        orm_mode = True

class DetallePedidoUpdate(BaseModel):
    cantidad: int
    precio_unitario: float
