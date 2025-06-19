from string import ascii_lowercase,ascii_uppercase


class Creatura():

    def __init__(self,nome:str=None):
        if nome != None:

            self.set_nome(nome)
        else:
            self.set_nome("Creatura Generica")

    def set_nome(self,nome:str=None)-> None:
        
        if type(nome) == str:
            self.nome = nome 
        if type(nome) == None:
            self.nome = "Creatura Generica"
     
    
    def get_nome(self)->str:
        return self.nome

    def __str__(self)-> str:
        return f"\nCreatura: {self.nome}"
    
