from services.usuario_service import UsuarioService
from repositories.usuario_repo import UsuarioRepository
from config.database import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Solicitando dados para o usuário.
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    print("\nListando usuários cadastrados.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - E-mail: {usuario.email} - Senha: {usuario.senha}")

if __name__ == "main":
    main()