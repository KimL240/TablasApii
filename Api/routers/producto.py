from fastapi import APIRouter, Depends, HTTPException
# Importa APIRouter para definir rutas, Depends para inyectar dependencias,
# y HTTPException para lanzar errores personalizados HTTP

from sqlmodel import Session, select
# Importa Session para manejar la base de datos y select para consultas SQLModel

from typing import List
# Importa List para definir el tipo de respuestas con múltiples elementos

from Api.database import get_session
# Importa la función que retorna la sesión activa de la base de datos

from Api.models.productos import Producto
# Importa el modelo Producto

from Api.schemas.productos import productoBase, productoCreate, productoRead, productoUpdate
# Importa los esquemas para lectura, creación, actualización y base del producto

router = APIRouter(prefix="/productos", tags=["productos"])
# Crea el router para los endpoints de productos con el prefijo '/productos'

@router.get("/", response_model=List[productoRead])
def get_productos(session: Session = Depends(get_session)):
    # Endpoint GET para obtener todos los productos
    productos = session.exec(select(Producto)).all()
    # Consulta todos los productos de la base de datos
    return productos

@router.get("/{id}", response_model=productoRead)
def get_producto(id: int, session: Session = Depends(get_session)):
    # Endpoint GET para obtener un producto específico por ID
    producto = session.get(Producto, id)
    if not producto:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Lanza error si el producto no existe
    return producto

@router.post("/", response_model=productoRead, status_code=201)
def create_producto(data: productoBase, session: Session = Depends(get_session)):
    # Endpoint POST para crear un nuevo producto
    nuevo = Producto(**data.dict())
    # Crea una instancia del modelo Producto usando los datos recibidos
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo
    # Retorna el producto creado

@router.put("/{id}", response_model=productoRead)
def update_producto(id: int, data: productoCreate, session: Session = Depends(get_session)):
    # Endpoint PUT para actualizar completamente un producto
    producto = session.get(Producto, id)
    if not producto:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Lanza error si no existe
    for key, value in data.dict().items():
        setattr(producto, key, value)
        # Actualiza todos los campos con los nuevos valores
    session.commit()
    session.refresh(producto)
    return producto

@router.patch("/{id}", response_model=productoRead)
def patch_producto(id: int, data: productoUpdate, session: Session = Depends(get_session)):
    # Endpoint PATCH para actualización parcial de un producto
    producto = session.get(Producto, id)
    if not producto:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(producto, key, value)
        # Actualiza solo los campos proporcionados
    session.commit()
    session.refresh(producto)
    return producto

@router.delete("/{id}")
def delete_producto(id: int, session: Session = Depends(get_session)):
    # Endpoint DELETE para eliminar un producto por ID
    producto = session.get(Producto, id)
    if not producto:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Lanza error si no se encuentra
    session.delete(producto)
    session.commit()
    return {"ok": True, "mensaje": "Producto eliminado correctamente"}
    # Retorna una respuesta de confirmación
