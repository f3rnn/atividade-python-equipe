import pytest

from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.enums.uf import UnidadeFederativa

@pytest.fixture
def engenheiro_valido():
    return Engenheiro("João","71965783567","joao@email.com","55698746",
                      Endereco("Via Alameda","95","Fim de linha",UnidadeFederativa.BAHIA,"Salvador"))

#Validando atributos
def test_nome_valido(engenheiro_valido):
    assert engenheiro_valido.nome == "João"

def test_telefone_valido(engenheiro_valido):
    assert engenheiro_valido.telefone == "71965783567"

def test_email_valido(engenheiro_valido):
    assert engenheiro_valido.email == "joao@email.com"

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "55698746"

#Validando atributos de endereco
def test_logradouro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.logradouro == "Via Alameda"