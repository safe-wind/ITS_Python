
from class_studente import Studente
from modulo import Modulo
class esame:

    class _link:

        modulo:Modulo
        studente:Studente
        voto:int

        def __init__(self, studente:Studente, modulo:Modulo, voto:int)-> None:
            self._studente = studente
            self._modulo = modulo
            self._voto = voto
            