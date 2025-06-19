from creatura import Creatura
import random

class Alieno(Creatura):

    def __init_subclass__(cls):
        return super().__init_subclass__()

    def __init__(self):
        self._matricola=""
        self._munizioni=[]
        self.nome = f"Robot-{self._set_matricola()}"
        self._set_munizioni()

    def get_nome(self):
        return self.nome
    
    def _set_matricola(self) -> None:
        self._matricola = random.randint(10000,90000)
        return self._matricola

    
    def _get_matricola(self) -> int:
        return self._matricola 
    
    def _set_munizioni(self):

        self._munizioni= [x * x for x in range(0,15)]
        return self._munizioni
    
    def __str__(self):
        return f"Alieno: {self.get_nome()}"
        



if __name__=="__main__":

    creatura:Creatura =Creatura("Creatur")
    alieno1:Alieno = Alieno()
    alieno1._set_matricola()
    print(alieno1.get_nome())
    print(alieno1)
    