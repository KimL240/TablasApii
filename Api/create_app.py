from fastapi import FastAPI
from sqlmodel import SQLModel
from Api.database import engine

def create_app():
    app= FastAPI()
    SQLModel.metadata.create_all(bind=engine)
    app.include_router()
    return app