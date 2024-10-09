import pytest

from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro, Funcionario

@pytest.fixture
def engenheiro_valido():
    return Engenheiro("Heloisa Elza", "33993097188", "heloisaelzacarvalho@kframe.com.br",
                  Endereco("Rua Aluízio Pereira Esteves", "701", "ali", "35032010", "Governador Valadares"),"654321")

def test_nome_valido(engenheiro_valido):
    assert engenheiro_valido.nome == "Heloisa Elza"

def test_telefone_valido(engenheiro_valido):
    assert engenheiro_valido.telefone == "33993097188"

def test_email_valido(engenheiro_valido):
    assert engenheiro_valido.email == "heloisaelzacarvalho@kframe.com.br"

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "654321"

def test_logradouro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.logradouro == "Rua Aluízio Pereira Esteves"

def test_numero_endereco_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.numero == "701"

def test_complemento_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.complemento == "ali"

def test_cep_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cep == "35032010"

def test_cidade_valida(engenheiro_valido):
    assert engenheiro_valido.endereco.cidade == "Governador Valadares"

def test_nome_vazio(engenheiro_valido):
    with pytest.raises(ValueError, match="o nome não pode estar vazio"):
        Engenheiro("", "33993097188", "heloisaelzacarvalho@kframe.com.br",
                  Endereco("Rua Aluízio Pereira Esteves", "701", "ali", "35032010", "Governador Valadares"),"654321")

def test_nome_invalido(engenheiro_valido):
    with pytest.raises(TypeError, match="o nome deve ser um texto"):
        Engenheiro(123, "33993097188", "heloisaelzacarvalho@kframe.com.br",
                  Endereco("Rua Aluízio Pereira Esteves", "701", "ali", "35032010", "Governador Valadares"),"654321")