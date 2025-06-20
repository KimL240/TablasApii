from sqlmodel import Session, create_engine
# Importa Session para manejar sesiones de base de datos
# Importa create_engine para crear la conexión a la base de datos

sql_name = 'Tablasapi.db'
# Nombre del archivo de la base de datos SQLite

sql_url = f'sqlite:///{sql_name}'
# URL de conexión para SQLite, usando el archivo definido arriba

engine = create_engine(sql_url, echo=True)
# Crea el engine de conexión a la base de datos
# echo=True habilita que se muestren en consola las consultas SQL ejecutadas

def get_session():
    # Función generadora para obtener una sesión de base de datos
    with Session(engine) as session:
        yield session
        # Cede la sesión para ser usada con Depends en FastAPI y la cierra al acabar
