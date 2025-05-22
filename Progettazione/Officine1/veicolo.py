from targa import Targa
import datetime
class Veicolo:

    def __init__(self,targa:Targa, anno_imm:datetime):
        
        self._targa = targa
        self._anno_imm = anno_imm
    
    def getAnnoImm(self) -> datetime:
        return self._anno_imm