from fastapi import APIRouter, Depends, HTTPException
# Importa APIRouter para definir rutas, Depends para inyectar dependencias,
# y HTTPException para lanzar errores HTTP personalizados

from sqlmodel import Session, select
# Importa Session para manejar la conexión con la base de datos
# y select para construir consultas SQLModel

from typing import List
# Importa List para tipado de listas

from Api.database import get_session
# Importa la función para obtener una sesión activa de base de datos

from Api.models.pedidos import Pedido
# Importa el modelo Pedido

from Api.schemas.pedidos import PedidoCreate, PedidoRead, PedidoUpdate
# Importa los esquemas para crear, leer y actualizar pedidos

router = APIRouter(prefix="/pedidos", tags=["pedidos"])
# Crea el router de la API con prefijo '/pedidos' y etiqueta 'pedidos'

@router.get("/", response_model=List[PedidoRead])
def get_pedidos(session: Session = Depends(get_session)):
    # Endpoint GET para obtener todos los pedidos
    return session.exec(select(Pedido)).all()
    # Ejecuta la consulta y devuelve todos los pedidos

@router.get("/{id}", response_model=PedidoRead)
def get_pedido(id: int, session: Session = Depends(get_session)):
    # Endpoint GET para obtener un pedido específico por ID
    pedido = session.get(Pedido, id)
    if not pedido:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Lanza error si no se encuentra el pedido
    return pedido

@router.post("/", response_model=PedidoRead, status_code=201)
def create_pedido(data: PedidoCreate, session: Session = Depends(get_session)):
    # Endpoint POST para crear un nuevo pedido
    nuevo = Pedido(**data.dict())
    # Crea una nueva instancia del modelo Pedido con los datos recibidos
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo
    # Devuelve el pedido recién creado

@router.put("/{id}", response_model=PedidoRead)
def update_pedido(id: int, data: PedidoCreate, session: Session = Depends(get_session)):
    # Endpoint PUT para actualizar completamente un pedido existente
    pedido = session.get(Pedido, id)
    if not pedido:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict().items():
        setattr(pedido, key, value)
        # Reemplaza todos los atributos con los nuevos valores
    session.commit()
    session.refresh(pedido)
    return pedido
    # Devuelve el pedido actualizado

@router.patch("/{id}", response_model=PedidoRead)
def patch_pedido(id: int, data: PedidoUpdate, session: Session = Depends(get_session)):
    # Endpoint PATCH para actualizar parcialmente un pedido
    pedido = session.get(Pedido, id)
    if not pedido:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(pedido, key, value)
        # Solo actualiza los campos que se enviaron (los demás quedan igual)
    session.commit()
    session.refresh(pedido)
    return pedido

@router.delete("/{id}")
def delete_pedido(id: int, session: Session = Depends(get_session)):
    # Endpoint DELETE para eliminar un pedido por su ID
    pedido = session.get(Pedido, id)
    if not pedido:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(pedido)
    session.commit()
    return {"ok": True, "mensaje": "Pedido eliminado correctamente"}
    # Devuelve un mensaje indicando que el pedido fue eliminado exitosamente
