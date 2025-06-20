from pydantic import BaseModel
# Importa BaseModel de Pydantic para crear y validar modelos de datos

class DetallePedidoBase(BaseModel):
    # Esquema base con los campos obligatorios comunes para DetallePedido
    pedido_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float

class DetallePedidoCreate(DetallePedidoBase):
    # Esquema usado para crear un nuevo detalle de pedido (hereda todo del base)
    pass

class DetallePedidoRead(DetallePedidoBase):
    # Esquema usado para leer datos del detalle del pedido
    class Config:
        orm_mode = True
        # Permite que Pydantic trabaje con objetos ORM como los de SQLModel

class DetallePedidoUpdate(BaseModel):
    # Esquema para actualizar parcialmente un detalle de pedido
    cantidad: int
    precio_unitario: float
    # ⚠️ Nota: no es un verdadero "PATCH" porque ambos campos son obligatorios aquí.
    # Si deseas que sea realmente parcial, deberías marcarlos como `Optional`
