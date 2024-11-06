from models.usuario import Usuario
from services.usuario_service import UsuarioService
from repositories.usuario_repo import UsuarioRepository
from config.database import Session
import os
import time


def exibir_menu():
    print("\nMenu:\n")
    print("1. Criar Usuário")
    print("2. Pesquisar um usuário")
    print("3. Atualizar dados de um usuário")
    print("4. Excluir um usuário")
    print("5. Exibir todos os usuários cadastrados")
    print("0. Sair\n")


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:

        exibir_menu()

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                os.system("cls||clear")
                nome = input("Digite seu nome: ")
                email = input("Digite seu e-mail: ")
                senha = input("Digite sua senha: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)

            case 2:
                os.system("cls||clear")
                service.pesquisar_usuario()

            case 3:
                os.system("cls||clear")
                service.atualizar_usuario()

            case 4:
                os.system("cls||clear")
                service.excluir_usuario()

            case 5:
                os.system("cls||clear")
                service.listar_todos_usuarios()
                time.sleep(3)

            case 0:
                os.system("cls||clear")
                break

            case _:
                print("\nOpção inválida.\n")


if __name__ == "__main__":
    main()
