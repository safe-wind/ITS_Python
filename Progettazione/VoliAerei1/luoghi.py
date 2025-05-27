from custom_types import *
from naz_cit_link import *

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
    naz_cit: naz_cit._link

    def __init__(self, nome:str, elenco_citta:set[Citta])-> None:

        self.setNome(nome)

    def setNome(self, nome:str)-> None:
        self._nome = nome
    
    def getNome(self) -> str:
        return self._nome