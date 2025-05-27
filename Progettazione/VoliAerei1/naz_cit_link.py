
from luoghi import *

class naz_cit:

    _citta:Citta 

    class _link:

        def __init__(self,citta:Citta) -> None:

            self._setCitta(citta)
            self._lista_di_citta = set()

        def setCitta(self, citta:Citta) -> None:
            self._citta = citta
            self.list_citta.append(self._citta)

        def getCitta(self) -> set:
            return self._lista_di_citta
        
        def rmvCitta(self,citta:Citta) -> None:
            self._lista_di_citta.remove(citta)
            
        
