from documento import Documento

class File(Documento):

    def __init__(self, nome_percorso:str):

        self.path = nome_percorso

        # metodi di file \
        #                \
        #                \
        #\\\\\\\\\\\\\\\\\

    def leggi_testo_da_file(self):

        with open(self.path,"r") as file:
            
            return file.read()
        
        # read.line() 1 riga alla volta
        #             utile con i cicli
        
        #redd.lines() 1 lista dove ogni
        #             elemento è una linea
