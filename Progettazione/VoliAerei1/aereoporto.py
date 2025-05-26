from custom_types import *
class Aereoporto:

    def __init__(self, cod:str, nome:str):
        self.cod = cod
        self.setNome(nome)

    def setNome(self, nome:str) -> None:
        self.nome = nome
    
    def getNome(self) -> str:
        return self.nome
