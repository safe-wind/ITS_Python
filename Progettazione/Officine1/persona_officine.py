from codfisc import CodiceFiscale

class Persona:

    # name = name
    # lastnm:str = lastname
    # cf:str = cod. fiscale
    # tel:str
    # indirizzo:str

    def __init__(self,name:str,last:str,cf:CodiceFiscale) -> None:

        self.setName(name)
        self.setLast(last)
        self.setCf(cf)

    

    

    