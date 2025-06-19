from creatura import Creatura
import random

class Alieno(Creatura):

    _matricola:int #int > 0
    
    def __init_subclass__(cls):
        return super().__init_subclass__()

    def __init__(self):
        
        self._set_matricola()
        self._set_munizioni()

    def _set_matricola(self) -> None:
        self._matricola = random.randint(10000,90000)
    
    def _get_matricola(self) -> int:
        return self._matricola
    
    def _sequenza_muniz(self, cont_sequenza:int=0, sequenza:int=0)->None:
        
        result =cont_sequenza+sequenza
        cont_sequenza+=1
        sequenza+=2
        
        return result
        
    
    def _set_munizioni(self):

        _munizioni:list[int] = list()
        
            
        return _munizioni



if __name__=="__main__":

    creatura:Creatura =Creatura("Creatur")
    alieno1:Alieno = Alieno()
    print(alieno1._set_munizioni())
    print(alieno1.get_nome())