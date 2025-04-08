

class Persona:

    def __init__(self, name:str):
        
        #il nome non può essere una stringa vuota
        if name:
            self.name = name
        else:
            print("You didn't put a name as paramater")


        
        pass    #####################################