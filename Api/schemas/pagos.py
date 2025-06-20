from pydantic import BaseModel
# Importa BaseModel para crear y validar esquemas de datos

from datetime import date
# Importa date para manejar fechas en los datos

from typing import Optional
# Importa Optional para campos que pueden ser omitidos en actualizaciones parciales

class PagoBase(BaseModel):
    # Esquema base con campos comunes para un pago
    pedido_id: int
    monto: float
    metodo_pago: str
    fecha_pago: date

class PagoCreate(PagoBase):
    # Esquema para crear un pago (hereda del esquema base)
    pass

class PagoRead(PagoBase):
    # Esquema para leer un pago, incluye el campo id
    id: int

    class Config:
        orm_mode = True
        # Permite trabajar con objetos ORM para respuestas

class PagoUpdate(BaseModel):
    # Esquema para actualización parcial de un pago
    pedido_id: Optional[int]
    monto: Optional[float]
    metodo_pago: Optional[str]
    fecha_pago: Optional[date]
    # Todos opcionales para permitir modificaciones parciales (PATCH)
