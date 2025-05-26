from custom_types import *
class Aereoporto:
    _cod:str #<<immutabile>>, noto alla nascita
    _nome:str # noto alla nascita

    def __init__(self, cod:str, nome:str):
        self._cod = cod
        self.setNome(nome)

    def setNome(self, nome:str) -> None:
        self.nome = nome
    
    def getNome(self) -> str:
        return self.nome

    def getCodice(self)->str:
        return self._cod