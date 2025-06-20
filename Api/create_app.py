from fastapi import FastAPI
from sqlmodel import SQLModel
from Api.database import engine
from fastapi import FastAPI
from Api.routers import (
    cliente, direcciones, categoria, producto,
    pedidos, detalle_pedidos, pagos, usuario
)


def create_app():
    app= FastAPI()
    SQLModel.metadata.create_all(bind=engine)
    app.include_router(usuario.router, prefix="/usuarios", tags=["Usuarios"])
    app.include_router(cliente.router, prefix="/clientes", tags=["Clientes"])
    app.include_router(direcciones.router, prefix="/direcciones", tags=["Direcciones"])
    app.include_router(categoria.router, prefix="/categorias", tags=["Categorias"])
    app.include_router(producto.router, prefix="/productos", tags=["Productos"])
    app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])
    app.include_router(detalle_pedidos.router, prefix="/detalles", tags=["Detalles"])
    app.include_router(pagos.router, prefix="/pagos", tags=["Pagos"])

    return app
    
