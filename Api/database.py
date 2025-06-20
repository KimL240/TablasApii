from sqlmodel import Session , create_engine

sql_name= 'Tablasapi.db'
sql_url= f'sqlite:///{sql_name}'
engine= create_engine(sql_url,echo=True)

def get_session():
    with Session(engine) as session:
        yield session
