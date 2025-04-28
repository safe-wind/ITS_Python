

class Persona:

    def __init__(self, name:str, lastname:str, age:int):
        
        self.setName(name)
        self.setLastName(lastname)
        self.setAge(age)
    
    def __str__(self):
        return f"\nNome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
    def setName(self, name:str) -> None:
        if name:
            self.name = name
    def setLastName(self, lastname:str) -> None:
        if lastname:
            self.lastname = lastname
    def setAge(self, age:int) -> None:
        if age:
            self.age = age

    def getName(self) -> str:
        return self.name
    def getLastName(self) -> str:
        return self.lastname 
    def getAge(self) -> int:
        return self.age 

    def speak(self) -> None:
        print(f"\nHello my name is {self.getName()}!\n")


