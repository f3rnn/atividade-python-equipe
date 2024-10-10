from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.endereco = endereco
    
    def _verificar_nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("apenas texto para nome")
        if not nome.strip():
            raise ValueError("nome não pode estar vazio")
        return nome
    
    def _verificar_telefone(self, telefone):
        if not telefone.strip():
            raise ValueError("telefone não pode estar vazio")
        return telefone

    def _verificar_email(self, email):
        if not email.strip():
            raise ValueError("email não pode estar vazio")
        return email
    
    def _verificar_salario(self, valor):
        if not isinstance(valor, float):
            raise TypeError("apenas números")
        if valor < 0:
            raise ValueError("apenas valores positivos para salário")
        return valor
    
    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"\nnome: {self.nome}"
                f"\ntelefone: {self.telefone}"
                f"\nemail: {self.email}"
                f"\nsalário: {self._verificar_salario(salario_final())}"
                f"\nendereço: {self.endereco}")