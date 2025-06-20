from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from Api.database import get_session
from Api.models.pedidos import Pedido
from Api.schemas.pedidos import PedidoCreate, PedidoRead, PedidoUpdate

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@router.get("/", response_model=List[PedidoRead])
def get_pedidos(session: Session = Depends(get_session)):
    return session.exec(select(Pedido)).all()

@router.get("/{id}", response_model=PedidoRead)
def get_pedido(id: int, session: Session = Depends(get_session)):
    pedido = session.get(Pedido, id)
    if not pedido:
        raise HTTPException(status_code=404, detail="No encontrado")
    return pedido

@router.post("/", response_model=PedidoRead, status_code=201)
def create_pedido(data: PedidoCreate, session: Session = Depends(get_session)):
    nuevo = Pedido(**data.dict())
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo

@router.put("/{id}", response_model=PedidoRead)
def update_pedido(id: int, data: PedidoCreate, session: Session = Depends(get_session)):
    pedido = session.get(Pedido, id)
    if not pedido:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict().items():
        setattr(pedido, key, value)
    session.commit()
    session.refresh(pedido)
    return pedido

@router.patch("/{id}", response_model=PedidoRead)
def patch_pedido(id: int, data: PedidoUpdate, session: Session = Depends(get_session)):
    pedido = session.get(Pedido, id)
    if not pedido:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(pedido, key, value)
    session.commit()
    session.refresh(pedido)
    return pedido

@router.delete("/{id}")
def delete_pedido(id: int, session: Session = Depends(get_session)):
    pedido = session.get(Pedido, id)
    if not pedido:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(pedido)
    session.commit()
    return {"ok": True, "mensaje": "Pedido eliminado correctamente"}
