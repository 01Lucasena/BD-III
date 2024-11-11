import os
import time
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from app.models.usuario import Usuario
from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repo import UsuarioRepository
from app.config.database import Session



def exibir_menu():
    print("\n=== SENAI SOLUTION ===:\n")
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
                service.excluir_usuario()

            case 5:
                service.listar_todos_usuarios()
                time.sleep(3)

            case 0:
                break

            case _:
                print("\nOpção inválida.\n")


if __name__ == "__main__":
    os.system("cls||clear")
    main()
