
from media import Media

class Movie(Media):
    #attributi superclasse media 
    #
    #
    def __init__(self, title:str, year:int, durata:int) -> None:
        
        super().__init__(title, year)
        
        self.setDurata(durata)

    def setDurata(self, durata:int)-> None:
        if durata >= 0:
            self.durata = durata
        else:
            print("Errore")

    def getDurata(self) -> int:
        return self.durata
    
    def __str__(self):
        return f"{super.__str__()}\nDurata: {self.getDurata}"