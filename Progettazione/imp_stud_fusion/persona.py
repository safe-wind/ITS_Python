

class Persona: 
    _nome: str
    _cognome: str
    _cf:CodiceFiscale
    _nascita: date # <<immutabile>>

    _is_uomo: bool
    _is_donna: bool
    _maternita: IntGEZ | None
    _posizione_militare:PosizioneMilitare | None


    def __init__(self, nome:str, cognome:str, cf:CodiceFiscale,
                 nascita:date, 
                 maternita:IntGEZ | None = None
                 posizione_militare: PosizioneMilitare | None = None):
    
        
        self.set_cognome(cognome)
        self.set_cf(cf)

        if maternita is not None:
            self.set_attributi_donna(maternita)

        if posizione_militare is not None:
            self.set_attributi_uomo(posizione_militare)

        if not (self.is_donna() or self.is_uomo()):
            raise ValueError()
    
    def set_attributi_donna(self, maternita:IntGEZ)-> None:
        self.maternita = maternita


    def set_nome(self,nome):
        pass
    def set_cognome(self,cognome):
        pass
    def set_cf(self,cf):
        pass


class PosizioneMilitare:
    _nome:str #id immutabile

    def __init__(self, nome:str) -> None:
        pass