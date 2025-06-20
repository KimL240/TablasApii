from fastapi import APIRouter, Depends, HTTPException
# Importa APIRouter para rutas, Depends para inyección de dependencias,
# y HTTPException para manejar errores HTTP personalizados

from sqlmodel import Session, select
# Importa Session para gestionar la base de datos y select para hacer consultas SQLModel

from typing import List
# Importa List para declarar respuestas como listas tipadas

from Api.database import get_session
# Importa la función que retorna la sesión de base de datos

from Api.models.pagos import Pago
# Importa el modelo Pago

from Api.schemas.pagos import PagoCreate, PagoRead, PagoUpdate
# Importa los esquemas para crear, leer y actualizar pagos

router = APIRouter(prefix="/pagos", tags=["pagos"])
# Crea el router para los endpoints relacionados con pagos

@router.get("/", response_model=List[PagoRead])
def get_pagos(session: Session = Depends(get_session)):
    # Endpoint GET que retorna la lista de todos los pagos
    return session.exec(select(Pago)).all()
    # Ejecuta la consulta y retorna todos los registros de la tabla Pago

@router.get("/{id}", response_model=PagoRead)
def get_pago(id: int, session: Session = Depends(get_session)):
    # Endpoint GET que obtiene un pago específico por su ID
    pago = session.get(Pago, id)
    # Busca el pago por ID
    if not pago:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Lanza un error 404 si no se encuentra
    return pago

@router.post("/", response_model=PagoRead, status_code=201)
def create_pago(data: PagoCreate, session: Session = Depends(get_session)):
    # Endpoint POST para crear un nuevo pago
    nuevo = Pago(**data.dict())
    # Crea una nueva instancia de Pago con los datos recibidos
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo
    # Retorna el nuevo pago creado

@router.put("/{id}", response_model=PagoRead)
def update_pago(id: int, data: PagoCreate, session: Session = Depends(get_session)):
    # Endpoint PUT para actualizar completamente un pago por su ID
    pago = session.get(Pago, id)
    if not pago:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Si no se encuentra, lanza un error 404
    for key, value in data.dict().items():
        setattr(pago, key, value)
        # Asigna cada campo nuevo al objeto pago
    session.commit()
    session.refresh(pago)
    return pago

@router.patch("/{id}", response_model=PagoRead)
def patch_pago(id: int, data: PagoUpdate, session: Session = Depends(get_session)):
    # Endpoint PATCH para actualizar parcialmente un pago por ID
    pago = session.get(Pago, id)
    if not pago:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(pago, key, value)
        # Solo actualiza los campos que fueron enviados (exclude_unset ignora los vacíos)
    session.commit()
    session.refresh(pago)
    return pago

@router.delete("/{id}")
def delete_pago(id: int, session: Session = Depends(get_session)):
    # Endpoint DELETE para eliminar un pago por ID
    pago = session.get(Pago, id)
    if not pago:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(pago)
    session.commit()
    return {"ok": True, "mensaje": "Pago eliminado correctamente"}
    # Retorna un mensaje indicando que el pago fue eliminado correctamente
