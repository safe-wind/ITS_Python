from persona_officine import Persona
from indirizzo import Indirizzo
from telefono import Telefono
from codfisc import CodiceFiscale

class Proprietario(Persona):

    def __init__(self, nm, lm, cf:CodiceFiscale, tel:Telefono, indirizzo:Indirizzo):
        super().__init__(nm, lm, cf, tel, indirizzo)
