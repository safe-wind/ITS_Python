from persona_officine import Persona
from indirizzo import Indirizzo
from telefono import Telefono
from codfisc import CodiceFiscale

class Dipendente(Persona):
     
    def __init__(self, name, last, cf:CodiceFiscale, tel:Telefono, indirizzo:Indirizzo):
        super().__init__(name, last, cf, tel, indirizzo)
