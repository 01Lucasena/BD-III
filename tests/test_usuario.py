import pytest
from app.models.usuario import Usuario

def test_usuario_erro_nome_vazio():
    with pytest.raises(TypeError,match="O nome não deve ficar vazio."):
        Usuario("","lucas@email.com","Lucas@123")

def test_usuario_erro_nome_invalido():
    with pytest.raises(TypeError,match="O nome deve ser um texto."):
        Usuario(123,"lucas@email.com","Lucas@123")

def test_usuario_erro_email_vazio():
    with pytest.raises(TypeError,match="O e-mail não deve ficar vazio."):
        Usuario("lucas","","Lucas@123")

def test_usuario_erro_email_invalido():
    with pytest.raises(TypeError,match="O e-mail deve ser um texto."):
        Usuario("lucas",123,"Lucas@123")

def test_usuario_erro_senha_tamanho():
    with pytest.raises(ValueError,match="A senha deve ter no mínimo 8 digitos."):
        Usuario("lucas","lucas@email.com","1234567")

def test_usuario_erro_senha_char_maiusculo():
    with pytest.raises(ValueError,match="A senha deve conter pelo menos uma letra MAIÚSCULA."):
        Usuario("lucas","lucas@email.com","123a5678")

def test_usuario_erro_senha_numero():
    with pytest.raises(ValueError,match="A senha deve conter pelo menos um NÚMERO."):
        Usuario("lucas","lucas@email.com","abcDefgh")

def test_usuario_erro_senha_char_especial():
    with pytest.raises(ValueError,match="A senha deve conter pelo menos um CARACTERE ESPECIAL."):
        Usuario("lucas","lucas@email.com","a2cDefgh")
