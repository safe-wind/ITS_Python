from codfisc import CodiceFiscale
from telefono import Telefono
from indirizzo import Indirizzo
class Persona:

    # name = name
    # lastnm:str = lastname
    # cf:str = cod. fiscale
    # tel:str
    # indirizzo:str

    def __init__(self,name:str,last:str,cf:CodiceFiscale, tel:Telefono,indirizzo:Indirizzo) -> None:

        self.setName(name)
        self.setLast(last)
        self.setCf(cf)
        self.setTel(tel)
        self.setIndirizzo(indirizzo)
    

    

    