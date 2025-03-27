

class Persona: #nome cognome ed eta sono attributi della classe persona

    #come posso renderli in python:
    #self.age
    #self.name
    #self.lastname

    #definisco un costruttore

    def __init__(self, name:str, last_name:str, age:int):
        self.name = name
        self.last_name = last_name
        self.age = age
    def __str__(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.last_name}\nAge: {self.age}"
    #funzione che mi consente di ritornare il valore self.name
    def getName(self) -> str:
        return self.name
    #funzione che mi consente di ritornare il valore self.last_name
    def getLastName(self) -> str:
        return self.last_name
    #funzione che mi consente di ritornare il valore self.age
    def getAge(self) -> int:
        return self.age
        