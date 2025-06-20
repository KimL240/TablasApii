from fastapi import APIRouter, Depends, HTTPException
# Importa APIRouter para definir rutas, Depends para inyectar dependencias,
# y HTTPException para manejar errores HTTP

from sqlmodel import Session, select
# Importa Session para conectarse a la base de datos y select para realizar consultas

from typing import List
# Importa List para definir el tipo de respuestas como listas

from Api.database import get_session
# Importa la función que retorna una sesión activa de la base de datos

from Api.models.detalle_pedidos import DetallePedido
# Importa el modelo DetallePedido

from Api.schemas.detalle_pedidos import DetallePedidoCreate, DetallePedidoRead, DetallePedidoUpdate
# Importa los esquemas para creación, lectura y actualización parcial de DetallePedido

router = APIRouter(prefix="/detalle-pedidos", tags=["detalle_pedidos"])
# Define el router con el prefijo de ruta y el tag para documentación

@router.get("/", response_model=List[DetallePedidoRead])
def get_detalles(session: Session = Depends(get_session)):
    # Endpoint GET que retorna todos los detalles de pedidos
    return session.exec(select(DetallePedido)).all()
    # Ejecuta la consulta y retorna todos los registros de la tabla DetallePedido

@router.get("/{pedido_id}/{producto_id}", response_model=DetallePedidoRead)
def get_detalle(pedido_id: int, producto_id: int, session: Session = Depends(get_session)):
    # Endpoint GET que busca un detalle de pedido por sus claves compuestas: pedido_id y producto_id
    detalle = session.get(DetallePedido, (pedido_id, producto_id))
    if not detalle:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Si no se encuentra, lanza excepción 404
    return detalle

@router.post("/", response_model=DetallePedidoRead, status_code=201)
def create_detalle(data: DetallePedidoCreate, session: Session = Depends(get_session)):
    # Endpoint POST para crear un nuevo detalle de pedido
    nuevo = DetallePedido(**data.dict())
    # Crea una nueva instancia del modelo usando los datos recibidos
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo
    # Retorna el detalle creado

@router.patch("/{pedido_id}/{producto_id}", response_model=DetallePedidoRead)
def patch_detalle(pedido_id: int, producto_id: int, data: DetallePedidoUpdate, session: Session = Depends(get_session)):
    # Endpoint PATCH para actualizar parcialmente un detalle de pedido usando claves compuestas
    detalle = session.get(DetallePedido, (pedido_id, producto_id))
    if not detalle:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(detalle, key, value)
        # Actualiza solo los campos enviados (no nulos)
    session.commit()
    session.refresh(detalle)
    return detalle
    # Retorna el detalle actualizado

@router.delete("/{pedido_id}/{producto_id}")
def delete_detalle(pedido_id: int, producto_id: int, session: Session = Depends(get_session)):
    # Endpoint DELETE para eliminar un detalle de pedido específico
    detalle = session.get(DetallePedido, (pedido_id, producto_id))
    if not detalle:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(detalle)
    session.commit()
    return {"ok": True, "mensaje": "Detalle eliminado correctamente"}
    # Retorna confirmación de eliminación
