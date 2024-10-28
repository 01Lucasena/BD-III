from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parâmetros de conexão com MySQL.
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# Endereço para conexão com o BD MySQL
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Conectando ao banco de dados.
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

#Gerenciando sessão.
@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commit() # Se der certo da commit.
    except Exception as erro:
        db.rollback() # Se der errado desfaz a operação
        raise erro
    finally:
        db.close()