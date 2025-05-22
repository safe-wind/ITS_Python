from persona_officine import Persona
from indirizzo import Indirizzo
from telefono import Telefono
from codfisc import CodiceFiscale
import datetime

class Direttore(Persona):

    def __init__(self, name, last, cf:CodiceFiscale, tel:Telefono, indirizzo:Indirizzo, data_nascita:datetime):
        super().__init__(name, last, cf, tel, indirizzo)

        self._data_nascita = data_nascita
    
    def getDataNascita(self) -> str:
        return self._data_nascita
        

        