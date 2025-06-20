from pydantic import BaseModel
# Importa BaseModel para crear y validar esquemas

from datetime import date
# Importa date para manejar fechas en los datos

from typing import Optional
# Importa Optional para campos que pueden no enviarse en actualizaciones parciales

class PedidoBase(BaseModel):
    # Esquema base con campos comunes para Pedido
    fecha: date
    cliente_id: int

class PedidoCreate(PedidoBase):
    # Esquema para creación de Pedido, hereda campos base
    pass

class PedidoRead(PedidoBase):
    # Esquema para lectura de Pedido, incluye campo id
    id: int

    class Config:
        orm_mode = True
        # Permite convertir objetos ORM a Pydantic

class PedidoUpdate(BaseModel):
    # Esquema para actualización parcial de Pedido
    fecha: Optional[date]
    cliente_id: Optional[int]
    # Ambos campos son opcionales para permitir PATCH parcial
