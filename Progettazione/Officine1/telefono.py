import re

class Telefono:

    def __init__(self,tel:str):

        self.setTel(tel)

    def setTel(self,tel:str):

        if not re.fullmatch(r"\+*[0-9]+{5,10}", tel):
            raise ValueError(f"Formato non corretto. Riprova. ({tel=})")
        
        else:
            self._tel = tel

    def getTel(self) -> str:
        return self._tel
    
    def __hash__(self) ->  int:
        return hash(self.getTel())
    
    def __eq__(self,other) -> bool:

        if hash(self) != hash(other):
            return None
        else:
            return self.getTel(self) == self.getTel(other)
        