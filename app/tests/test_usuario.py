import pytest
from app.models.usuario import Usuario


@pytest.fixture

def usuario_valido():
    Usuario("lucas", "lucas@email.com", "lucas123")

def test_nome_valido(usuario_valido):
    assert usuario_valido.nome == "lucas"

def test_email_valido(usuario_valido):
    assert usuario_valido.email == "lucas@email.com"

def test_nome_valido(usuario_valido):
    assert usuario_valido.senha == "lucas123"

def test_usuario_erro_nome_vazio(usuario_valido):
    with pytest.raises(ValueError,match="O nome não pode estar vazio."):
        Usuario("","lucas@email.com","lucas123")

def test_usuario_erro_nome_invalido(usuario_valido):
    with pytest.raises(ValueError,match="O nome deve ser um texto."):
        Usuario("123","lucas@email.com","lucas123")