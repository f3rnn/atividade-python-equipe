from projeto.models.enums.uf import UnidadeFederativa

class Endereco:
    def __init__(self,logradouro:str,numero:str,complemento:str,uf:UnidadeFederativa,cidade:str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.uf = uf
        self.cidade = cidade

    def __str__(self) -> str:
        return(
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nUF: {self.uf.sigla}"
            f"\nCidade: {self.cidade}"
        )