import pytest

from projeto.models.endereco import Endereco
from projeto.models.medico import Medico

@pytest.fixture
def medico_valido():
    return Medico("Heloisa Elza", "33993097188", "heloisaelzacarvalho@kframe.com.br", "123456",
                  Endereco("Rua Aluízio Pereira Esteves", "701", "ali", "35032010", "Governador Valadares"))

def test_nome_valido(medico_valido):
    assert medico_valido.nome == "Heloisa Elza"

def test_telefone_valido(medico_valido):
    assert medico_valido.telefone == "33993097188"

def test_email_valido(medico_valido):
    assert medico_valido.email == "heloisaelzacarvalho@kframe.com.br"

def test_crm_valido(medico_valido):
    assert medico_valido.crm == "123456"

def test_logradouro_valido(medico_valido):
    assert medico_valido.endereco.logradouro == "Rua Aluízio Pereira Esteves"

def test_numero_endereco_valido(medico_valido):
    assert medico_valido.endereco.numero == "701"

def test_complemento_valido(medico_valido):
    assert medico_valido.endereco.complemento == "ali"

def test_cep_valido(medico_valido):
    assert medico_valido.endereco.cep == "35032010"

def test_cidade_valida(medico_valido):
    assert medico_valido.endereco.cidade == "Governador Valadares"