
import random

# Classe base: Creatura
class Creatura:
    def __init__(self, nome: str):
        self.__nome = nome if isinstance(nome, str) else "Creatura Generica"

    def setNome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            self.__nome = "Creatura Generica"

    def getNome(self) -> str:
        return self.__nome

    def __str__(self):
        return f"Creatura: {self.__nome}"