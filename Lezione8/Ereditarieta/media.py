
class Media:

    def __init__(self, title:str, year:int) -> None:
        self.setTitle(title)
        self.setYear(year)
    
    def __str__(self):
        return f"Tirolo {self.getTitle()}, ANNO {self.getYear()}"

    def setTitle(self, title:str) ->None:
        if title:
            self.title = title
        else: 
            print("Erroere")
    
    def setYear(self, year:int) -> None:
        if year>1900:
            self.year = year
        else:
            print("Errore")

    
    def getTitle(self) -> str:
        return self.title
    def getYear(self) -> int:
        return self.year