from fastapi import APIRouter, Depends, HTTPException
# Importa APIRouter para definir rutas de la API,
# Depends para inyectar la sesión de base de datos,
# y HTTPException para lanzar errores personalizados

from sqlmodel import Session, select
# Importa Session para operaciones con la base de datos,
# y select para construir consultas

from Api.database import get_session
# Importa la función que devuelve una sesión activa de la base de datos

from Api.models.usuario import Usuario
# Importa el modelo Usuario

from Api.schemas.usuario import UsuarioCreate, UsuarioRead, UsuarioUpdate
# Importa los esquemas de entrada y salida (Create, Read, Update)

router = APIRouter()
# Crea el router principal sin prefijo (puede añadirse desde la app principal)

@router.get("/", response_model=list[UsuarioRead])
def get_usuarios(session: Session = Depends(get_session)):
    # Endpoint GET para listar todos los usuarios
    return session.exec(select(Usuario)).all()
    # Ejecuta la consulta y devuelve todos los usuarios

@router.get("/{id}", response_model=UsuarioRead)
def get_usuario(id: int, session: Session = Depends(get_session)):
    # Endpoint GET para obtener un usuario específico por ID
    usuario = session.get(Usuario, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Lanza error 404 si no existe el usuario
    return usuario

@router.post("/", response_model=UsuarioRead)
def create_usuario(usuario: UsuarioCreate, session: Session = Depends(get_session)):
    # Endpoint POST para crear un nuevo usuario
    nuevo = Usuario(**usuario.dict())
    # Crea una instancia del modelo Usuario con los datos recibidos
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo
    # Devuelve el usuario recién creado

@router.put("/{id}", response_model=UsuarioRead)
def update_usuario(id: int, data: UsuarioCreate, session: Session = Depends(get_session)):
    # Endpoint PUT para actualizar completamente un usuario
    usuario = session.get(Usuario, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="No encontrado")
        # Lanza error si no se encuentra el usuario
    for key, value in data.dict().items():
        setattr(usuario, key, value)
        # Asigna nuevos valores a cada campo
    session.commit()
    return usuario

@router.patch("/{id}", response_model=UsuarioRead)
def patch_usuario(id: int, data: UsuarioUpdate, session: Session = Depends(get_session)):
    # Endpoint PATCH para actualizar parcialmente un usuario
    usuario = session.get(Usuario, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="No encontrado")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(usuario, key, value)
        # Solo actualiza los campos enviados
    session.commit()
    return usuario

@router.delete("/{id}")
def delete_usuario(id: int, session: Session = Depends(get_session)):
    # Endpoint DELETE para eliminar un usuario por ID
    usuario = session.get(Usuario, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(usuario)
    session.commit()
    return {"ok": True}
    # Devuelve confirmación de eliminación
