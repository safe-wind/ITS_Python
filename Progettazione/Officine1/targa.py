import re

class Targa:

    def __init__(self, targa:str):
        
        self.setTarga(targa)

    def setTarga(self,targa:str) -> None:

        if not re.fullmatch(r"$[A-Z]{2}[0-9]{3}[A-Z]{2}^ | $[A-Z]{2}[0-9]{5}^", targa):
            raise ValueError("targa inserita non rispetta requisiti")
        else:
            self._targa = targa
    
    def getTarga(self) -> str:
        return self._targa
    