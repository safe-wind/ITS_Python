import re

class CodiceFiscale:

    def  __init__(self,cf:str) -> None:
        
        self.setCf(cf)

    def setCf(self, cf) -> None:

        if not re.fullmatch(r"[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}", cf):
            print("Codice fiscale non corretto")

        else:
            self._cf =cf 

    def getCf(self) -> str:
        return self._cf
    
    def __hash__(self):
        return hash(self._cf)
    
    def __eq__(self, other):
        if other is None or not isinstance(other, type(self)) or hash(other) != hash(self):
            return False
        else:
            return self.getCf() == other.getCf()
        

# cf1= CodiceFiscale("GDLMRS01R05Z140J")
# cf2= CodiceFiscale("GDLMRS01R05Z140J")

# print(cf1.__eq__(cf2))


