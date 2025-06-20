from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from Api.database import get_session
from Api.models.pagos import Pago
from Api.schemas.pagos import PagoCreate, PagoRead, PagoUpdate

router = APIRouter(prefix="/pagos", tags=["pagos"])

@router.get("/", response_model=List[PagoRead])
def get_pagos(session: Session = Depends(get_session)):
    return session.exec(select(Pago)).all()

@router.get("/{id}", response_model=PagoRead)
def get_pago(id: int, session: Session = Depends(get_session)):
    pago = session.get(Pago, id)
    if not pago:
        raise HTTPException(status_code=404, detail="No encontrado")
    return pago

@router.post("/", response_model=PagoRead, status_code=201)
def create_pago(data: PagoCreate, session: Session = Depends(get_session)):
    nuevo = Pago(**data.dict())
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo

@router.put("/{id}", response_model=PagoRead)
def update_pago(id: int, data: PagoCreate, session: Session = Depends(get_session)):
    pago = session.get(Pago, id)
    if not pago:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict().items():
        setattr(pago, key, value)
    session.commit()
    session.refresh(pago)
    return pago

@router.patch("/{id}", response_model=PagoRead)
def patch_pago(id: int, data: PagoUpdate, session: Session = Depends(get_session)):
    pago = session.get(Pago, id)
    if not pago:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(pago, key, value)
    session.commit()
    session.refresh(pago)
    return pago

@router.delete("/{id}")
def delete_pago(id: int, session: Session = Depends(get_session)):
    pago = session.get(Pago, id)
    if not pago:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(pago)
    session.commit()
    return {"ok": True, "mensaje": "Pago eliminado correctamente"}
