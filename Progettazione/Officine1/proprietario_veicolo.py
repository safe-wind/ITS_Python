from persona_officine import Persona

class Proprietario(Persona):

    def __init__(self, nm, lm, cf, tel, indirizzo):
        super().__init__(nm, lm, cf, tel, indirizzo)
