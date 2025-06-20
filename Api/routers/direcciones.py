from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from Api.database import get_session
from Api.models.direcciones import direcciones as Direccion
from Api.schemas.direcciones import DireccionBase, DireccionCreate, DireccionRead, DireccionUpdate

router = APIRouter(prefix="/direcciones", tags=["direcciones"])

@router.get("/", response_model=List[DireccionRead])
def get_direcciones(session: Session = Depends(get_session)):
    direcciones = session.exec(select(Direccion)).all()
    return direcciones

@router.post("/", response_model=DireccionRead)
def create_direcciones(data: DireccionCreate, session: Session = Depends(get_session)):
    nueva = Direccion(**data.dict())
    session.add(nueva)
    session.commit()
    session.refresh(nueva)
    return nueva

@router.put("/{id}", response_model=DireccionRead)
def update_direcciones(id: int, data: DireccionCreate, session: Session = Depends(get_session)):
    direccion = session.get(Direccion, id)
    if not direccion:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict().items():
        setattr(direccion, key, value)
    session.commit()
    session.refresh(direccion)
    return direccion

@router.patch("/{id}", response_model=DireccionRead)
def patch_direcciones(id: int, data: DireccionUpdate, session: Session = Depends(get_session)):
    direccion = session.get(Direccion, id)
    if not direccion:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(direccion, key, value)
    session.commit()
    session.refresh(direccion)
    return direccion

@router.delete("/{id}")
def delete_direcciones(id: int, session: Session = Depends(get_session)):
    direccion = session.get(Direccion, id)
    if not direccion:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(direccion)
    session.commit()
    return {"ok": True, "mensaje": "Dirección eliminada correctamente"}
