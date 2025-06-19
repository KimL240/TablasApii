from sqlmodel import Session , create_engine

sql_name= 'Tablasapi'
sql_url= f'sqliteñ:///{sql_name}'
engine= create_engine(sql_url,echo=True)

def get_session():
    with Session(engine) as session:
        yield session
