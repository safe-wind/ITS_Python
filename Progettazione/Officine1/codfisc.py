import re

class CodiceFiscale:

    def  __init__(self,cf:str) -> None:
        
        if not re.fullmatch(r"[A-Z]{6}/d{2}[A-Z]{1}/d{2}[A-Z]{1}/d{3}[A-Z]{1}", cf):
            print("Codice fiscale non corretto")

        else:
            self.cf

        
