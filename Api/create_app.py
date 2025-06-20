from fastapi import FastAPI
# Importa la clase FastAPI para crear la aplicación

from sqlmodel import SQLModel
# Importa SQLModel para gestionar el esquema y las tablas en la base de datos

from Api.database import engine
# Importa el engine (conexión a la base de datos)

from Api.routers import (
    cliente, direcciones, categoria, producto,
    pedidos, detalle_pedidos, pagos, usuario
)
# Importa todos los routers que contienen los endpoints por módulo

def create_app():
    # Función para crear y configurar la instancia de la aplicación FastAPI
    app = FastAPI()
    # Crea la app FastAPI

    SQLModel.metadata.create_all(bind=engine)
    # Crea las tablas en la base de datos si no existen, según los modelos

    app.include_router(usuario.router, prefix="/usuarios", tags=["Usuarios"])
    # Incluye el router de usuarios con prefijo y etiqueta para documentación
    app.include_router(cliente.router, prefix="/clientes", tags=["Clientes"])
    app.include_router(direcciones.router, prefix="/direcciones", tags=["Direcciones"])
    app.include_router(categoria.router, prefix="/categorias", tags=["Categorias"])
    app.include_router(producto.router, prefix="/productos", tags=["Productos"])
    app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])
    app.include_router(detalle_pedidos.router, prefix="/detalles", tags=["Detalles"])
    app.include_router(pagos.router, prefix="/pagos", tags=["Pagos"])
    # Se registran todos los routers para que sus rutas formen parte de la API

    return app
    # Devuelve la instancia de la aplicación configurada
