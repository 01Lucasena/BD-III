from models.usuario import Usuario
from services.usuario_service import UsuarioService
from repositories.usuario_repo import UsuarioRepository
from config.database import Session


def exibir_menu():
    print("Menu:")
    print("1. Criar Usuário")
    print("2. Pesquisar um usuário")
    print("3. Atualizar dados de um usuário")
    print("4. Excluir um usuário")
    print("5. Exibir todos os usuários cadastrados")
    print("0. Sair")


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        exibir_menu()

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                # Solicitando dados para o usuário.
                nome = input("Digite seu nome: ")
                email = input("Digite seu e-mail: ")
                senha = input("Digite sua senha: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)

                
            case 2:
                print("\nListando usuários cadastrados.")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(
                        f"Nome: {usuario.nome} - E-mail: {usuario.email} - Senha: {usuario.senha}"
                    )
                print("Pesquisando usuário.")
                email = input("Digite o e-mail do usuário: ")
                pesquisaUsuario = session.query(Usuario).filter_by(email = email).first()
                print(pesquisaUsuario)
                


            case 3:
                print("Atualizando dados do usuário.")
                email = input("Digite o e-mail do usuário: ")
                usuario = session.query(Usuario).filter_by(email=email).first()

                if usuario:
                    nome = input("Digite seu nome: ")
                    email = input("Digite seu e-mail: ")
                    senha = input("Digite sua senha: ")

                    session.commit()
                else:
                    print("Usuário não encontrado.")
            
            case 4:
                print("Deletando dados do usuário.")
                email = input("Digite o e-mail do usuário: ")
                usuario = session.query(Usuario).filter_by(email=email).first()

                if usuario:
                    session.delete(usuario)
                    session.commit()
                    print(f"Usuário {usuario.nome} excluído com sucesso.")
                
                else:
                    print("Usuário não encontrado.")
            case 5:
                print("\nListando usuários cadastrados.")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(
                        f"Nome: {usuario.nome} - E-mail: {usuario.email} - Senha: {usuario.senha}"
                    )
            case 0:
                break

            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
