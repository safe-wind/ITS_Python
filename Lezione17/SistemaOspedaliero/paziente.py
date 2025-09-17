
from persona import Persona

class Paziente(Persona):
    def __init__(self, nome, cognome, eta, idCode):
        super().__init__(nome, cognome, eta)
        self.__idCode = idCode

    def setIdCode(self, idCode):
        self.__idCode = idCode

    def getidCode(self):
        return self.__idCode

    def patientInfo(self):
        print(f"Paziente: {self.nome} {self.cognome}\nID: {self.__idCode}")