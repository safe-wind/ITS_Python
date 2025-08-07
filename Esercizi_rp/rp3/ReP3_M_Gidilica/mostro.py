from creatura import Creatura
from alieno import Alieno
import random

class Mostro(Creatura):
    def __init__(self, nome: str, vittoria: str, sconfitta: str):
        super().__init__(nome)
        self.__setVittoria(vittoria)
        self.__setSconfitta(sconfitta)
        self.__setAssalto()

    def __setVittoria(self, vittoria: str):
        self.__urlo_vittoria = vittoria if isinstance(vittoria, str) else "GRAAAHHH"

    def __setSconfitta(self, sconfitta: str):
        self.__gemito_sconfitta = sconfitta if isinstance(sconfitta, str) else "Uuurghhh"

    def __setAssalto(self):
        self.__assalto = random.sample(range(1, 101), 15)

    def getAssalto(self) -> list:
        return self.__assalto

    def getVittoria(self) -> str:
        return self.__urlo_vittoria

    def getSconfitta(self) -> str:
        return self.__gemito_sconfitta

    def __str__(self):
        nome = self.getNome()
        alt_nome = ''.join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(nome)])
        return f"Mostro: {alt_nome}"

# Funzione pariUguali
def pariUguali(a: list[int], b: list[int]) -> list[int]:
    return [1 if a[i] % 2 == 0 and b[i] % 2 == 0 else 0 for i in range(min(len(a), len(b)))]

# Funzione combattimento
def combattimento(a: Alieno, m: Mostro):
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Errore: oggetti non validi per il combattimento.")
        return None

    esito = pariUguali(a.getMunizioni(), m.getAssalto())
    if esito.count(1) > 4:
        for _ in range(3):
            print(m.getVittoria())
        return m
    else:
        print(m.getSconfitta())
        return a

# Funzione proclamaVincitore
def proclamaVincitore(c: Creatura):
    testo = str(c)
    lunghezza = len(testo) + 10
    for i in range(5):
        for j in range(lunghezza):
            if i == 0 or i == 4 or j == 0 or j == lunghezza - 1:
                print("*", end="")
            elif i == 2 and j == 5:
                print(testo, end="")
                print(" " * (lunghezza - len(testo) - 6) + "*", end="")
                break
            else:
                print(" ", end="")
        print()