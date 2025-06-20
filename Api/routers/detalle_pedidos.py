from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from Api.database import get_session
from Api.models.detalle_pedidos import DetallePedido
from Api.schemas.detalle_pedidos import DetallePedidoCreate, DetallePedidoRead, DetallePedidoUpdate

router = APIRouter(prefix="/detalle-pedidos", tags=["detalle_pedidos"])

@router.get("/", response_model=List[DetallePedidoRead])
def get_detalles(session: Session = Depends(get_session)):
    return session.exec(select(DetallePedido)).all()

@router.get("/{pedido_id}/{producto_id}", response_model=DetallePedidoRead)
def get_detalle(pedido_id: int, producto_id: int, session: Session = Depends(get_session)):
    detalle = session.get(DetallePedido, (pedido_id, producto_id))
    if not detalle:
        raise HTTPException(status_code=404, detail="No encontrado")
    return detalle

@router.post("/", response_model=DetallePedidoRead, status_code=201)
def create_detalle(data: DetallePedidoCreate, session: Session = Depends(get_session)):
    nuevo = DetallePedido(**data.dict())
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo

@router.patch("/{pedido_id}/{producto_id}", response_model=DetallePedidoRead)
def patch_detalle(pedido_id: int, producto_id: int, data: DetallePedidoUpdate, session: Session = Depends(get_session)):
    detalle = session.get(DetallePedido, (pedido_id, producto_id))
    if not detalle:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(detalle, key, value)
    session.commit()
    session.refresh(detalle)
    return detalle

@router.delete("/{pedido_id}/{producto_id}")
def delete_detalle(pedido_id: int, producto_id: int, session: Session = Depends(get_session)):
    detalle = session.get(DetallePedido, (pedido_id, producto_id))
    if not detalle:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(detalle)
    session.commit()
    return {"ok": True, "mensaje": "Detalle eliminado correctamente"}
