from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str,crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
    
    def _verificar_email(self, email):
        return super()._verificar_email(email)
    
    def _verificar_nome(self, nome):
        return super()._verificar_nome(nome)
    
    def _verificar_telefone(self, telefone):
        return super()._verificar_telefone(telefone)
    
    def salario_final(self) -> float:
        return 10000.0
    
    def _verificar_salario(self, valor):
        return super()._verificar_salario(valor)
    
    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\ncrm: {self.crm}")