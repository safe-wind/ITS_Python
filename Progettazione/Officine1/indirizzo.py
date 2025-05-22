import re

class Indirizzo:

    def __init__(self, via:str, civico:str, cap:str) -> None:
        self.setVia(via)
        self.setCivico(civico)
        self.setCap(cap)

    def setVia(self,via:str)-> None:

        if via is None:
            raise ValueError("\'via\' can't be empty.")
        else:
            self._via = via

    def setCivico(self, civico:str) -> None:
        self._civico = civico

    def setCap(self, cap:str) -> None:
        if not re.fullmatch("[0-9]{5}"):
            raise ValueError("Cap value doesn't seem correct.")
        else:
            self._cap = cap
    
    def getVia(self) -> str:
        return self._via
    
    def getCivico(self) -> str:
        return self._civico
    
    def getCap(self) -> str:
        return self._cap

    def __hash__(self):
        return hash(self._cap, self._civico, self._via)
    
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)) or hash(self.getVia())!=hash(other.getVia()):
            return False
        else:
            return hash(self.getVia(),self.getCivico(),self.getCap())==hash(other.getVia(),other.getCivico(),other.getCapetCap())
    