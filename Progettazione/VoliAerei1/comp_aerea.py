from custom_types import *
from luoghi import*
class CompAerea:

    _nome:str # noto alla nascita
    _anno_fondaz:IntG1900 #<<immutabile>>
    _comp_direz_citta:Citta  #noto alla nascita e mutabile

    def __init__(self, nome:str, anno_fondaz:IntG1900, citta_sede:Citta):
        self.setNome(nome) 
        self.anno_fondaz = anno_fondaz
        self.setCittaSede(citta_sede)

        
    def setNome(self, nome) -> None:
        self.nome = nome
    
    def getNome(self) -> str:
        return self._nome

    def getAnnoFondaz(self) -> IntG1900:
        return self._anno_fondaz
    
    def citta_sede(self) -> Citta:
        return self._comp_direz_citta
    
    def setCittaSede(self, c:Citta) -> None:
        self._comp_direz_citta = c