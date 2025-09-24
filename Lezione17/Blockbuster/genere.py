from film import Film

class Azione(Film):

    def __init__(self, id, title):
        super().__init__(id, title)
        self._genere = "Azione"
        self._penale = 3.0

    def getGenere(self)-> str:
        
        return self._genere
    
    def getPenale(self)->float:
        return self._penale 
    
    def calcolaPenaleRitardo(self, gg_ritardo:int) -> float:

        return float(gg_ritardo*self._penale)

#############################################################################

class Commedia(Film):

    def __init__(self, id, title):
        super().__init__(id, title)
        self._genere = "Commedia"
        self._penale = 2.50

    def getGenere(self)-> str:
        return self._genere
    
    def getPenale(self)->float:
        return self._penale 
    
    def calcolaPenaleRitardo(self, gg_ritardo:int) -> float:

        return float(gg_ritardo*self._penale)
    
##########################################################################   

class Drama(Film):

    def __init__(self, id, title):
        super().__init__(id, title)
        self._genere = "Drama"
        self._penale = 2.0

    def getGenere(self)-> str:
        
        return self._genere
    
    def getPenale(self)->float:
        return self._penale 
    
    def calcolaPenaleRitardo(self, gg_ritardo:int) -> float:

        return float(gg_ritardo*self._penale)
    

    
