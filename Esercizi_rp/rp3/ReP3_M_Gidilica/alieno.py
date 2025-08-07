from creatura import Creatura
import random
# Classe derivata: Alieno
class Alieno(Creatura):
    def __init__(self):
        self.__setMatricola()
        self.__setMunizioni()
        nome_alieno = f"Robot-{self.__matricola}"
        super().__init__(nome_alieno)
        if not nome_alieno.startswith("Robot-"):
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            self.setNome(f"Robot-{self.__matricola}")

    def __setMatricola(self):
        self.__matricola = random.randint(10000, 90000)

    def __setMunizioni(self):
        self.__munizioni = [i*i for i in range(15)]

    def getMatricola(self) -> int:
        return self.__matricola

    def getMunizioni(self) -> list:
        return self.__munizioni

    def __str__(self):
        return f"Alieno: {self.getNome()}"
