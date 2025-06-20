from fastapi import APIRouter, Depends, HTTPException
# Importa APIRouter para definir rutas, Depends para inyectar dependencias,
# y HTTPException para lanzar errores HTTP personalizados

from sqlmodel import Session, select
# Importa Session para manejar la base de datos y select para realizar consultas SQLModel

from typing import List
# Importa List para declarar respuestas con múltiples elementos

from Api.database import get_session
# Importa la función que proporciona la sesión de conexión a la base de datos

from Api.models.direcciones import direcciones as Direccion
# Importa el modelo 'direcciones' y lo renombra como 'Direccion' para seguir convención PascalCase

from Api.schemas.direcciones import DireccionBase, DireccionCreate, DireccionRead, DireccionUpdate
# Importa los esquemas de validación y serialización para la entidad 'direcciones'

router = APIRouter(prefix="/direcciones", tags=["direcciones"])
# Define el router de FastAPI con el prefijo '/direcciones' y la etiqueta 'direcciones' para documentación

@router.get("/", response_model=List[DireccionRead])
def get_direcciones(session: Session = Depends(get_session)):
    # Endpoint GET que retorna la lista de todas las direcciones
    direcciones = session.exec(select(Direccion)).all()
    # Ejecuta la consulta para seleccionar todas las direcciones
    return direcciones

@router.post("/", response_model=DireccionRead)
def create_direcciones(data: DireccionCreate, session: Session = Depends(get_session)):
    # Endpoint POST para crear una nueva dirección
    nueva = Direccion(**data.dict())
    # Crea una nueva instancia del modelo Dirección con los datos recibidos
    session.add(nueva)
    # Añade la nueva dirección a la sesión
    session.commit()
    # Guarda los cambios en la base de datos
    session.refresh(nueva)
    # Refresca el objeto para obtener campos generados automáticamente (como el id)
    return nueva

@router.put("/{id}", response_model=DireccionRead)
def update_direcciones(id: int, data: DireccionCreate, session: Session = Depends(get_session)):
    # Endpoint PUT para actualizar completamente una dirección por su id
    direccion = session.get(Direccion, id)
    # Busca la dirección por id
    if not direccion:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Lanza error si no se encuentra la dirección
    for key, value in data.dict().items():
        setattr(direccion, key, value)
        # Actualiza cada campo con los nuevos valores
    session.commit()
    session.refresh(direccion)
    return direccion

@router.patch("/{id}", response_model=DireccionRead)
def patch_direcciones(id: int, data: DireccionUpdate, session: Session = Depends(get_session)):
    # Endpoint PATCH para actualizar parcialmente una dirección por su id
    direccion = session.get(Direccion, id)
    # Busca la dirección
    if not direccion:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Lanza error si no existe
    for key, value in data.dict(exclude_unset=True).items():
        setattr(direccion, key, value)
        # Solo actualiza los campos que se enviaron (exclude_unset ignora los no enviados)
    session.commit()
    session.refresh(direccion)
    return direccion

@router.delete("/{id}")
def delete_direcciones(id: int, session: Session = Depends(get_session)):
    # Endpoint DELETE para eliminar una dirección por id
    direccion = session.get(Direccion, id)
    # Busca la dirección
    if not direccion:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Lanza error si no existe
    session.delete(direccion)
    session.commit()
    return {"ok": True, "mensaje": "Dirección eliminada correctamente"}
    # Retorna un mensaje de confirmación
