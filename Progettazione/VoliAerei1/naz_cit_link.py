
from luoghi import Citta


class naz_cit:

    _citta:Citta

    class _link:

        def __init__(self,citta:Citta) -> None:

            self._setCitta(citta)
            self._lista_di_citta = set()

        def addCitta(self, citta:Citta) -> None:

            self.list_citta.append(citta)

        def getCitta(self) -> frozenset:
            return frozenset(self._lista_di_citta)
        
  
        
