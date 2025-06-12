import re
from datetime import *
from __future__ import annotations

class Importo(float):
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
    def __init__(self, nome:str, telefono:Telefono):
        
        self._nome = nome
        self._telefono = telefono

    def telefono(self)-> None:
        return self.telefono
    
    def nome(self)-> None:
        return self.nome
    
    def set_telefono(self, telefono:Telefono):
        self._telefono = telefono
        
    def set_nome(self, nome:str):
        self._nome = nome
        
class Impiegato:

    _nome:str #noto alla nascita
    _cognome:str #noto alla nascita
    _nascita:datetime.date # immutabile, noto alla nascita
    _stipendio:Importo #noto alla nascita
    _afferenza:afferenza
    

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
    def nascita(self) -> datetime:
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
    
class afferenza:
    _impiegato:Impiegato
    _dipartimento:Dipartimento
    _data_afferenza:datetime

    def __init__(self, impiegato:Impiegato, dipartimento,data_afferenza):
        self._impiegato = impiegato
        self._dipartimento = dipartimento
        self._data_afferenza = data_afferenza
        
    def setImpiegato(self,impiegato):
        self.impiegato = impiegato
    def setDipartimento(self,dipartimento):
        self.dipartimento = dipartimento
    def impiegato(self):
        return self.impiegato
    def dipartimento(self):
        pass
    def data_afferenza(self):
        pass 

class Progetto:
    _nome:str
    _budget:Importo
    _impiegati_prog:dict[Impiegato,_imp_prog] = () #certamente non noto alla nascita

    def __init__(self,nome:str,budget:Importo) -> None:
        self._nome:str = nome
        self._budget:Importo = budget
        #self._impiegati_prog:dict[Impiegato,date] = dict()

    def nome(self):
        return self._nome
    def budget(self):
        return self._budget
    def setBudget(self, budget:Importo):
        self._budget = budget
    def is_coinvolto(self,impiegato:Impiegato) -> bool:
        for coinvolto in self._coinvolti:
            if coinvolto.impiegato() == impiegato:
                return True
        return False
    
    
    '''def add_impiegato(self, impiegato:Impiegato) -> None:
        
        data_inizio_progetto:date = date.today()
        
        if impiegato not in  self._impiegati_prog:
            self._impiegati_prog[impiegato] = data_inizio_progetto
        else:
            raise ValueError(f"L'impiegato {impiegato.nome()} è già nel progetto")

    def remove_impiegato(self, impiegato:Impiegato) -> None:

        if impiegato in self._impiegati_prog:
            self._impiegati_prog.remove(impiegato)
        else:
            raise ValueError("Impiegato not in the project") 

    def get_impiegati_progetti(self)-> frozenset:
        return frozenset(self._impiegati_prog.items())'''

class _imp_prog:
    _progetto: Progetto
    _impiegato: Impiegato
    _data:date

    def progetto(self) -> Progetto:
        return self._progetto
    def impiegato(self) -> Impiegato:
        return self._progetto
    def data(self) -> date:
        return self.data

    def __hash__(self) -> int:
        return hash(self.progetto(),self.impiegato())
        
    def __eq__(self, other) -> bool:

        pass

print("\n\n________________Progetti________________\n")

pegaso: Progetto = Progetto(nome="Pegaso", budget=Importo(25000))

oggi = date.today()
domani = date.today()