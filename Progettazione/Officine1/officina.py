from indirizzo import Indirizzo


class Officina:

    def __init__(self,nome:str,indirizzo:Indirizzo) -> None:

        self._nome = nome
        self._indirizzo = indirizzo

    def getNome(self):
        return self._nome
    def getIndirizzo(self):
        return self._indirizzo
        