from models.usuario import Usuario
from repositories.usuario_repo import UsuarioRepository

class UsuarioService:
    def __init__(self,repository: UsuarioRepository ):
        self.repository = repository
    
    def criar_usuario(self,nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            novo_usuario = self.repository.pesquisar_usuario_por_email(usuario.email)

            if not novo_usuario:
                print("Usuário já cadastrado!")

            self.repository.salvar_usuario(usuario)
            print("Usuario cadastrado com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado {erro}")
    
    def pesquisar_usuario(self):
        try:
            print("\nPesquisando usuário.\n")
            email_usuario = input("Digite o e-mail do usuário: ")
            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email_usuario)

            if usuario_cadastrado:
                print(f"{usuario_cadastrado.nome} - {usuario_cadastrado.email} - {usuario_cadastrado.senha}")
            
            else:
                print("Usuário não encontrado")
                return
       
        except TypeError as erro:
            print(f"Erro ao buscar usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado {erro}") 
    
    def atualizar_usuario(self):
        try:
            print("\nAtualizando dados do usuário.\n")
            email_usuario = input("Digite o e-mail do usuário: ")
            usuario_cadastrado = self.repository.atualizar_usuario(email_usuario)
                
        
            if usuario_cadastrado:
                usuario_cadastrado.nome = input("Digite seu nome: ")
                usuario_cadastrado.email = input("Digite seu e-mail: ")
                usuario_cadastrado.senha = input("Digite sua senha: ")
                self.repository.atualizar_usuario(usuario_cadastrado)
                print("\nUsuário atualizado com sucesso.")  

            else:
                print("\nUsuário não encontrado.\n")
                return
        
        except TypeError as erro:
            print(f"Erro ao atualizar usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
       
    
    def listar_todos_usuarios(self):
        return self.repository.listar_usuario()
    
    def excluir_usuario(self):
        try:
            print("\nExcluindo dados do usuário.\n")
            email_usuario = input("Digite o e-mail do usuário: ")
            usuario_cadastrado = self.repository.atualizar_usuario(email_usuario)
        
            if usuario_cadastrado:
                senha_usuario = input("Digite a senha do usuário: ")

                if senha_usuario == usuario_cadastrado.senha:
                    self.repository.excluir_usuario(usuario_cadastrado)
            
                else:
                    print("Senha inválida.")
                    return
            else:
                print("\nUsuário não encontrado.\n")
                return
        
        except TypeError as erro:
            print(f"Erro ao deletar usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
