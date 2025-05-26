from modulo import *
from esame import *
class Studente:
    _nome:str
    _esami: esame._link

    def __init__(self, nome:str)-> None:
        self._nome = nome
        self._esami = dict()

    def nome(self) -> str:
        return self._nome
    
    def esami(self)-> frozenset[esame._link]:
        return frozenset(self._esami.values())
    
    def add_esame(self, modulo:Modulo, voto:int) -> None:
        if modulo in self._esami:
            raise KeyError("Gia' superato questo modulo")
        
        l: esame._link = esame._link(studente=self, modulo=modulo, voto=voto)
        self._esami[modulo] = l
    

    