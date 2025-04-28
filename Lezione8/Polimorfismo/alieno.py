
class Alieno:
    # self.galaxy:str
    def __init__(self, galaxy:str) -> None:

        self.setGalaxy(galaxy)
    
    def __str__(self) -> str:
        return f"Alieno da galassia {self.getGalaxy()}"
    
    def setGalaxy(self, galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else: 
            print("Errore. La galassia non può essere nulla")
    
    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print(f"\nblovlolvo\n")