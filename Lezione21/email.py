from documento import Documento

class Email(Documento):
    

    def get_test(self):
        return #stringa formattata
    
    def write_to_file(self, path:str) -> None:
        #>>>with open(path,modalita)
        # modalita: a = append
        #           w = write e sostituisce 
        #               il contenuto del file
        with open(path, "w") as file:
            file.write(self.get_test())

test: Email = Email()

test.write_to_file("./email.txt")