import pytest

from projeto.models.endereco import Endereco
from projeto.models.enums.uf import UnidadeFederativa
from projeto.models.medico import Medico

@pytest.fixture
def medico_valido():
    return Medico("dejair", "12345", "dejair@", "6543321",
                  Endereco("alameda", 123, "esquina", UnidadeFederativa.BAHIA, "salvador"))

def nome_valido(medico_valido):
    assert medico_valido.nome == "dejair"

def telefone_valido(medico_valido):
    assert medico_valido.telefone == "12345"

def email_valido(medico_valido):
    assert medico_valido.email == "dejair@"

def crm_valido(medico_valido):
    assert medico_valido.crm == "6543321"

def logradouro_valido(medico_valido):
    assert medico_valido.endereco.logradouro == "alameda"

def numero_valido(medico_valido):
    assert medico_valido.endereco.numero == "esquina"

def uf_valido (medico_valido):
    assert medico_valido.endereco.uf == UnidadeFederativa.BAHIA

def cidade_valido(medico_valido):
    assert medico_valido.endereco.cidade == "salvador"