from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario


class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco,crea:str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        return 10000.0
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCREA: {self.crea}")
    
    def _verificar_nome(self, valor):
        return super()._verificar_nome(valor)