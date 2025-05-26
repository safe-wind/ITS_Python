from custom_types import *
from datetime import datetime
class Volo:

    _cod:str #<<immutabile>>, noto alla nascita
    _durata_minuti: IntGZ #noto alla nascita

    def __init__(self, cod:str, durata:IntGZ):
        self._cod = cod
        self.setDurata(durata)

    def getCodice(self) -> str:
        return self._cod

    def setDurata(self, durata:IntGZ) -> None:
        self._durata = IntGZ(durata)

    def getDurata(self) -> IntGZ:
        return self._durata
    

volo1 = Volo("12345B", 140)