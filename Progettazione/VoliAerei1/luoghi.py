from custom_types import *

class Citta:
    _nome:str
    _abitanti:IntGEZ

    def __init__(self, nome:str, abitanti:IntGEZ):
        self.setNome(nome)
        self.setAbitanti(abitanti)
        

    def nome(self) -> str:
        return self._nome
    
    def setNome(self, nome:str) -> None:
        self._nome= nome

    def setAbitanti(self, abitanti:IntGEZ) -> None:
        self._abitanti = abitanti
    
    def getAbitanti(self) -> IntGEZ:
        return self._abitanti
    
class Nazione:

    _nome:str

    def __init__(self, nome:str)-> None:

        self.setNome(nome)

    def setNome(self, nome:str)-> None:
        self._nome = nome
    
    def getNome(self) -> str:
        return self._nome