
import datetime

class Riparazione:

    def __init__(self, codice:str, accettazione:datetime):

        self._codice = codice
        self.setAccettazione = accettazione

    def getCodice(self):
        return self._codice
    def getAccettazione(self):
        return self._accettazione
        
        