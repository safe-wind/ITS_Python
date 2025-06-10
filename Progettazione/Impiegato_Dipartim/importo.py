import re
from datetime import *

class Importo:
    def __new__(cls, valore:int|float|str):
        if valore < 0:
            raise ValueError("Not possible")
        return float.__new__(cls, valore)
    

class Telefono(str):
    def __new__(cls, telefono:str):
        if not re.fullmatch(r'\+?[0-9]+', telefono):
            raise ValueError()
        return str.__new__(cls, telefono)

class Dipartimento:
    _nome:str # noto alla nascita
    _telefono: Telefono # noto alla nascita
    pass    



class Impiegato:

    _nome:str #noto alla nascita
    _cognome:str #noto alla nascita
    _nascita:datetime.date # immutabile, noto alla nascita
    _stipendio:Importo #noto alla nascita
    #_dipartimento:Dipartimento #link afferenza

    def __init__(self, nome:str, cognome:str, nascita:datetime.date,stipendio:Importo,dipartimento:Dipartimento)-> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self.nascita = nascita
        self.set_stipendio(stipendio)
        self.set_dipartimento(Dipartimento)


    def nome(self) -> str:
        return self._nome
    def cognome(self) -> str:
        return self._cognome
    def nascita(self) -> datetime.date:
        return self._nascita
    def stipendio(self)-> Importo:
        return self._stipendio
    def set_nome(self, v:str) -> None:
        self._nome = v
    def set_cognome(self, v:str) -> None:
        self._cognome = v
    def set_stipendio(self, v:Importo) -> None:
        self._stipendio = v
    def set_dipartimento(self,v:Dipartimento) -> None:
        self._dipartimento = v
    def get_dipartimento(self) -> Dipartimento:
        return self._dipartimento
    def set_afferenza(self, dipartimento:Dipartimento, data:datetime.date):
        link = afferenza("anna", dipartimento, afferenza)
    
class afferenza:
    impiegato:Impiegato
    dipartimento:Dipartimento
    #data_afferenza #:datatime.date

    def __init__(self, impiegato, dipartimento,data_afferenza):
        pass
    def impiegato(self):
        pass
    def dipartimento(self):
        pass
    def data_afferenza(self):
        pass 
