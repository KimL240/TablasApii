from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from Api.database import get_session
from Api.models.clientes import Cliente
from Api.schemas.clientes import ClienteCreate, ClienteRead, ClienteUpdate

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.get("/", response_model=List[ClienteRead])
def listar_clientes(session: Session = Depends(get_session)):
    clientes = session.exec(select(Cliente)).all()
    return clientes

@router.get("/{cliente_id}", response_model=ClienteRead)
def obtener_cliente(cliente_id: int, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.post("/", response_model=ClienteRead, status_code=201)
def crear_cliente(cliente: ClienteCreate, session: Session = Depends(get_session)):
    nuevo_cliente = Cliente(**cliente.dict())
    session.add(nuevo_cliente)
    session.commit()
    session.refresh(nuevo_cliente)
    return nuevo_cliente

@router.put("/{cliente_id}", response_model=ClienteRead)
def actualizar_cliente(cliente_id: int, datos: ClienteCreate, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    for campo, valor in datos.dict().items():
        setattr(cliente, campo, valor)

    session.commit()
    session.refresh(cliente)
    return cliente

@router.patch("/{cliente_id}", response_model=ClienteRead)
def actualizar_parcial_cliente(cliente_id: int, datos: ClienteUpdate, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    for campo, valor in datos.dict(exclude_unset=True).items():
        setattr(cliente, campo, valor)

    session.commit()
    session.refresh(cliente)
    return cliente

@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    session.delete(cliente)
    session.commit()
    return {"ok": True, "mensaje": "Cliente eliminado correctamente"}
