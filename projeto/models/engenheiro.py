from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea
    
    def _verificar_nome(self, nome):
        return super()._verificar_nome(nome)
    
    def _verificar_email(self, email):
        return super()._verificar_email(email)
    
    def salario_final(self) -> float:
        return 5000.0
    
    def _verificar_salario(self, valor):
        return super()._verificar_salario(valor)
    
    def _verificar_telefone(self, telefone):
        return super()._verificar_telefone(telefone)
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\ncrea: {self.crea}")