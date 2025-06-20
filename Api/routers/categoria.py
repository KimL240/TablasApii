from fastapi import APIRouter, Depends, HTTPException
# Importa APIRouter para crear rutas, Depends para dependencias y HTTPException para errores HTTP

from sqlmodel import Session, select
# Importa Session para manejo de sesiones en la base de datos y select para consultas

from typing import List
# Importa List para tipado de listas

from Api.database import get_session
# Importa la función que provee la sesión de base de datos

from Api.models.categoria import categoria as Categoria
# Importa el modelo Categoria (con alias para mayúscula)

from Api.schemas.categoria import categoriaRead, categoriaCreate, categoriaBase, categriaUpdate
# Importa los schemas para validación y serialización de categorías (nota: typo en 'categriaUpdate')

router = APIRouter(prefix="/categorias", tags=["categorias"])
# Define un router para endpoints bajo la ruta base /categorias y con etiqueta "categorias"

@router.get("/", response_model=List[categoriaRead])
def get_categorias(session: Session = Depends(get_session)):
    # Endpoint GET para obtener todas las categorías
    categorias = session.exec(select(Categoria)).all()
    # Ejecuta una consulta para obtener todas las categorías
    return categorias
    # Retorna la lista de categorías

@router.post("/", response_model=categoriaRead)
def create_categoria(categoria: categoriaCreate, session: Session = Depends(get_session)):
    # Endpoint POST para crear una nueva categoría, recibe datos validados con categoriaCreate
    nuevo = Categoria(**categoria.dict())
    # Crea una instancia del modelo con los datos recibidos
    session.add(nuevo)
    # Añade el nuevo objeto a la sesión
    session.commit()
    # Guarda los cambios en la base de datos
    session.refresh(nuevo)
    # Actualiza el objeto con los datos guardados (por ejemplo, id autogenerado)
    return nuevo
    # Retorna el nuevo objeto creado

@router.put("/{id}", response_model=categoriaRead)
def update_categoria(id: int, data: categoriaCreate, session: Session = Depends(get_session)):
    # Endpoint PUT para actualizar una categoría completa por id
    categoria = session.get(Categoria, id)
    # Busca la categoría por id
    if not categoria:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Si no existe, lanza error 404
    for key, value in data.dict().items():
        setattr(categoria, key, value)
        # Actualiza todos los campos con los datos recibidos
    session.commit()
    # Guarda los cambios en la base de datos
    session.refresh(categoria)
    # Refresca el objeto actualizado
    return categoria
    # Retorna la categoría actualizada

@router.patch("/{id}", response_model=categoriaRead)
def patch_categoria(id: int, data: categriaUpdate, session: Session = Depends(get_session)):
    # Endpoint PATCH para actualización parcial de categoría por id
    categoria = session.get(Categoria, id)
    # Busca la categoría por id
    if not categoria:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Si no existe, lanza error 404
    for key, value in data.dict(exclude_unset=True).items():
        setattr(categoria, key, value)
        # Actualiza solo los campos que se enviaron en la petición
    session.commit()
    # Guarda los cambios
    session.refresh(categoria)
    # Refresca el obj
