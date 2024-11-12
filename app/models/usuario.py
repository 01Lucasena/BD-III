from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db


Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = self._verificar_nome(nome)
        self.email = self._verificar_email(email)
        self.senha = self._verificar_senha(senha)


    # Métodos
    def _verificar_nome(self, valor):
        
        self._verificar_nome_invalido(valor)
        self._verificar_nome_vazio(valor)
       
        self.nome = valor
        return self.nome
        
    def _verificar_email(self, valor):
       
        self._verificar_email_invalido(valor)
        self._verificar_email_vazio(valor)
       
        self.email = valor
        return self.email
   
    def _verificar_senha(self,password):
        
        self._verificar_senha_tamanho(password)
        self._verificar_senha_char_maiusculo(password)
        self._verificar_senha_tamanho(password)
        self._verificar_senha_char_maiusculo(password)
        self._verificar_senha_numero(password)
        self._verificar_senha_char_especial(password)

        self.senha = password
        return self.senha
       
    # Métodos Auxiliares
    def _verificar_nome_vazio(self, valor):

        if not valor.strip():
            raise TypeError("O nome não deve ficar vazio.")

    def _verificar_nome_invalido(self, valor):

        if not isinstance(valor, str):
            raise TypeError("O nome deve ser um texto.")

    def _verificar_email_vazio(self, valor):
       
        if not valor.strip():
           raise TypeError("O e-mail não deve ficar vazio.") 
        
    def _verificar_email_invalido(self, valor):

        if not isinstance(valor, str):
            raise TypeError("O e-mail deve ser um texto.")
        
    def _verificar_senha_tamanho(self, password):
        tamanho = len(password)

        if tamanho < 8:
            raise ValueError("A senha deve ter no mínimo 8 digitos.")
        
    def _verificar_senha_char_maiusculo(self, password):

        if password.islower():
            raise ValueError("A senha deve conter pelo menos uma letra MAIÚSCULA.")

    def _verificar_senha_numero(self, password):

        if password.isalpha():
            raise ValueError("A senha deve conter pelo menos um NÚMERO.")

    def _verificar_senha_char_especial(self, password):

        if password.isalnum():
            raise ValueError("A senha deve conter pelo menos um CARACTERE ESPECIAL.") 

Base.metadata.create_all(bind=db)
