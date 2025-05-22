
from riparazione import Riparazione
import datetime

class RiparazioneTerminata(Riparazione):

    def __init__(self, codice, accettazione, riconsegna:datetime):
        super().__init__(codice, accettazione)

        self.setRiconsegna(riconsegna)

    def setRiconsegna(self, riconsegna):
        self._riconsegna = riconsegna
    
    def getRiconsegna(self):
        return self._riconsegna