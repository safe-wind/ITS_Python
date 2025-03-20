
class Persona:

    def __init__(self):

        self.name = ""
        self.last_name = ""
        self.age = 0
        # voglio definire una funzione che mostri in output i dati di una persona

    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.last_name}\nEtà: {self.age}")

    #una funzione che ci consenta di impostare il valore self.name
    def setName(self, name:str) -> None:
        self.name = name

    #definisco una funzione che ci consenta di impostare il valore di self.lastname
    def setLastName(self, last_name:str) -> None:
        self.last_name = last_name
    def setAge(self, age:int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age
