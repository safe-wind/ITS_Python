from film import Film

class Azione(Film):

    def __init__(self, id, title, genere:str="Azione", penale:float=3.0):
        super().__init__(id, title)
        self._genere = genere
        self._penale = penale

    def getGenere(self)-> str:
        
        return self._genere
    
    def getPenale(self)->float:
        return self._penale 
    
    def calcolaPenaleRitardo(self, gg_ritardo:int) -> float:

        return float(gg_ritardo*self._penale, 2)

#############################################################################

class Commedia(Film):

    def __init__(self, id, title, genere:str="Commedia", penale:float=2.50):
        super().__init__(id, title)
        self._genere = genere
        self._penale = penale

    def getGenere(self)-> str:
        return self._genere
    
    def getPenale(self)->float:
        return self._penale 
    
    def calcolaPenaleRitardo(self, gg_ritardo:int) -> float:

        return float(gg_ritardo*self._penale, 2)
    
##########################################################################   

class Drama(Film):

    def __init__(self, id, title, genere:str="Drama", penale:float=2.0):
        super().__init__(id, title)
        self._genere = genere
        self._penale = penale

    def getGenere(self)-> str:
        
        return self._genere
    
    def getPenale(self)->float:
        return self._penale 
    
    def calcolaPenaleRitardo(self, gg_ritardo:int) -> float:

        return float(gg_ritardo*self._penale, 2)
    

    
