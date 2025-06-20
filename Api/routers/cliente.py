from fastapi import APIRouter, Depends, HTTPException
# Importa APIRouter para definir rutas, Depends para inyectar dependencias,
# y HTTPException para manejar errores HTTP

from sqlmodel import Session, select
# Importa Session para manejo de sesiones con la base de datos y select para consultas SQLModel

from typing import List
# Importa List para el tipado de listas

from Api.database import get_session
# Importa la función que obtiene la sesión de la base de datos

from Api.models.clientes import Cliente
# Importa el modelo Cliente desde la carpeta de modelos

from Api.schemas.clientes import ClienteCreate, ClienteRead, ClienteUpdate
# Importa los esquemas para validación y serialización de datos de Cliente

router = APIRouter(prefix="/clientes", tags=["clientes"])
# Crea el router de la API con prefijo /clientes y grupo de etiquetas "clientes"

@router.get("/", response_model=List[ClienteRead])
def listar_clientes(session: Session = Depends(get_session)):
    # Endpoint GET que retorna la lista de todos los clientes
    clientes = session.exec(select(Cliente)).all()
    # Ejecuta la consulta y obtiene todos los registros de la tabla Cliente
    return clientes

@router.get("/{cliente_id}", response_model=ClienteRead)
def obtener_cliente(cliente_id: int, session: Session = Depends(get_session)):
    # Endpoint GET que retorna un cliente específico por su ID
    cliente = session.get(Cliente, cliente_id)
    # Busca al cliente por ID
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
        # Lanza una excepción si el cliente no existe
    return cliente

@router.post("/", response_model=ClienteRead, status_code=201)
def crear_cliente(cliente: ClienteCreate, session: Session = Depends(get_session)):
    # Endpoint POST para crear un nuevo cliente
    nuevo_cliente = Cliente(**cliente.dict())
    # Crea una nueva instancia del modelo Cliente con los datos recibidos
    session.add(nuevo_cliente)
    # Añade el nuevo cliente a la sesión
    session.commit()
    # Confirma los cambios en la base de datos
    session.refresh(nuevo_cliente)
    # Actualiza el objeto con datos actuales de la BD (como el ID generado)
    return nuevo_cliente

@router.put("/{cliente_id}", response_model=ClienteRead)
def actualizar_cliente(cliente_id: int, datos: ClienteCreate, session: Session = Depends(get_session)):
    # Endpoint PUT para actualizar completamente un cliente por su ID
    cliente = session.get(Cliente, cliente_id)
    # Busca el cliente
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
        # Si no existe, lanza excepción
    for campo, valor in datos.dict().items():
        setattr(cliente, campo, valor)
        # Asigna los nuevos valores a los atributos del cliente
    session.commit()
    session.refresh(cliente)
    return cliente

@router.patch("/{cliente_id}", response_model=ClienteRead)
def actualizar_parcial_cliente(cliente_id: int, datos: ClienteUpdate, session: Session = Depends(get_session)):
    # Endpoint PATCH para actualizar parcialmente un cliente (solo campos enviados)
    cliente = session.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    for campo, valor in datos.dict(exclude_unset=True).items():
        setattr(cliente, campo, valor)
        # Solo actualiza los campos que se enviaron en la petición
    session.commit()
    session.refresh(cliente)
    return cliente

@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int, session: Session = Depends(get_session)):
    # Endpoint DELETE para eliminar un cliente por ID
    cliente = session.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    session.delete(cliente)
    session.commit()
    return {"ok": True, "mensaje": "Cliente eliminado correctamente"}
    # Retorna una respuesta de éxito
