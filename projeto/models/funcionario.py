from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = self._verificar_nome(nome)
        self.telefone = telefone
        self.email = self._verificar_email(email)
        self.endereco = endereco

    def _verificar_nome(self,valor):
            self.verificar_nome_vazio_invalido(valor)
            self.verificar_nome_tipo_invalido(valor)
            return valor

    def _verificar_email(self, valor):
        self.verificar_email_tipo_invalido(valor)
        self.verificar_email_vazio_invalido(valor)
        return valor
    
    @abstractmethod
    def salario_final(self) -> float:
        pass

    def verificar_nome_tipo_invalido(self,valor):
        if isinstance(valor,str):
            raise TypeError("o nome deve ser um texto")
        return valor

    def verificar_nome_vazio_invalido(self,valor):
        if not valor.strip():
            raise ValueError("o nome não pode estar vazio")
        return valor

    def verificar_email_tipo_invalido(self,valor):
        if isinstance(valor,str):
            raise TypeError("o email deve ser um texto")
        return valor
    
    def verificar_email_vazio_invalido(self,valor):
        if not valor.strip():
            raise ValueError("o email não pode estar vazio")
        return valor

    def __str__(self) -> str:
        return (
            f"\nnome: {self.nome}"
            f"\ntelefone: {self.telefone}"
            f"\ne-mail: {self.email}"
            f"\nendereço: {self.endereco}")