from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from Api.database import get_session
from Api.models.direcciones import direcciones
from Api.schemas.direcciones import DireccionBase, DireccionCreate, DireccionRead, DireccionUpdate

router=APIRouter()

@router.get('/', response_model=list[DireccionRead])
def get_direcciones(session: Session=Depends(get_session)):
    direcciones=session.get(direcciones, id)
    if not direcciones:
        raise HTTPException(status_code=404, detail="No encontrado")
    return direcciones

@router.post('/', response_model=DireccionRead)
def create_direcciones(direcciones: DireccionBase, session: Session=Depends(get_session)):
    nuevo = direcciones(**direcciones.dict())
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return direcciones

@router.put('/{id}', response_model=DireccionRead)
def update_direcciones(id: int, data: DireccionCreate, session: Session= Depends(get_session)):
    direcciones=Session.get(direcciones, id)
    if not direcciones:
        raise HTTPException(status_code=404, detail='No encontrado')
    for key, value in data.dict().items():
        setattr(direcciones, key, value)
    session.commit()
    return direcciones

@router.patch('/{id}', response_model=DireccionRead)
def patch_direcciones(id: int, data: DireccionUpdate, session: Session= Depends(get_session)):
    direcciones= session.get(direcciones, id)
    if not direcciones:
        raise HTTPException(status_code=404, detail='No encontrado')
    for key, Value in data.dict(exclude_unset=True).items():
        setattr(direcciones, key, Value)
    session.commit()
    return direcciones

@router.delete('/{id}')
def delete_direcciones(id: int, session: Session= Depends(get_session)):
    direcciones=session.get(direcciones, id)
    if not direcciones:
        raise HTTPException(status_code=404, detail='No encontrado')
    session.delete(direcciones)
    session()
    return{'ok':True}




