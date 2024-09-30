from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str,
                 endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
    
    def salario_final(self) -> float:
        return 15000.0
    
    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\ncrm: {self.crm}")