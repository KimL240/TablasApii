from sqlmodel import SQLModel, Field, Relationship
# Importa las clases necesarias de SQLModel para definir modelos, campos y relaciones

from typing import Optional, List, TYPE_CHECKING
# Importa herramientas de tipado: Optional para campos opcionales,
# List para listas tipadas y TYPE_CHECKING para evitar importaciones circulares

if TYPE_CHECKING:
    from Api.models.productos import Producto
    # Solo se importa Producto si se está haciendo verificación de tipos estática (no en tiempo de ejecución)
    # Esto evita problemas de dependencia circular

class categoria(SQLModel, table=True):
    # Define una clase 'categoria' como modelo de tabla en la base de datos

    id: Optional[int]= Field(default=None, primary_key=True)
    # Campo 'id' opcional, se autogenera y es clave primaria

    nombre: str
    # Campo obligatorio que representa el nombre de la categoría

    unidad: str
    # Campo obligatorio que representa la unidad de medida (por ejemplo: kg, litro, etc.)

    productos: List['Producto']=Relationship(back_populates='categoria')
    # Define una relación uno-a-muchos con el modelo Producto (una categoría puede tener muchos productos)
    # 'back_populates' indica que en Producto debe haber un campo 'categoria' que completa la relación
