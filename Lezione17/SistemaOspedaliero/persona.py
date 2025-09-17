class Persona:

    _nome:str
    _cognome:str
    _eta:int
    
    def __init__(self, nome:str, cognome:str, eta:int)-> None:

        if isinstance(nome, str) == False:
            self._nome = None
            raise ValueError("Il nome deve essere una stringa")
        else:
            self._nome= nome

        if isinstance(cognome, str) == False:
            self._cognome = None
            raise ValueError("Il cognome deve essere una stringa")
        else:
            self._cognome = cognome

        if self._cognome  == str and self._nome == str:
            self._eta = 0
        else:
            self._eta = None

    def setName(self, nome:str) -> None:
        if type(nome) is not str:
            self._nome = None
            raise ValueError("Il nome deve essere una stringa")
        else:
            self._nome = nome
    
    def setLastName(self, cognome:str)-> None:
        if type(cognome) is not str:
            self._cognome=None
            raise ValueError("Il cognome deve essere una stringa")
        else:
            self._cognome = cognome
    
    def setAge(self, eta:int) -> None:

        if type(eta) is not int and eta >= 0:
            self._eta=None
            raise ValueError("L'età deve essere un numero intero > 0")
        else:
            self._eta = eta
        
    def getName(self) -> str:
        return self._nome
    
    def getLastName(self) -> str:
        return self._cognome
    
    def getAge(self) -> int:
        return int(self._eta)
    
    def greet(self) -> None:
        print(f"Ciao, sono {self.getName()} {self.getLastName()}! Ho {self.getAge()} anni!")
    


