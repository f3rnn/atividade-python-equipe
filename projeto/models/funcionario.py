from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"\nnome: {self.nome}"
            f"\ntelefone: {self.telefone}"
            f"\ne-mail: {self.email}"
            f"\nendereço: {self.endereco}")