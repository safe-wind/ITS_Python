
from genere import Azione, Commedia, Drama
from film import Film

class Noleggio:


    def __init__(self, film_list:list[Azione|Commedia|Drama])-> None:
        
        self.flag:bool = None
        self.film_list = film_list

        self.rented_film:dict[int, list[Azione|Commedia|Drama]] = {}


    def isAvaible(self, film:Film)-> bool:
        #se è disponibile nell'Inventario negozio
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
            
        else:
            print(f"Il film scelto non è disponibile: {film.getTitle()}!")
            return False
    
    def rentAMovie(self,film:Azione | Commedia | Drama, clientID:int):
        #
        if self.isAvaible(film) == True:

            self.film_list.remove(film)

            for k, v in self.rented_film.items():

                if clientID == k:

                    v.append(film)

            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")

        else:
            print(f"Non è possibile nolegiare il film {film.getTitle()}!")

    def giveBack(self, film:Azione | Commedia | Drama, clientID:int, days:int)->None:

        for k, v in self.rented_film.items():

            if clientID == k:

                v.remove(film)
                self.film_list.append(film)
            
        print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} e' di {film.calcolaPenaleRitardo(days)} euro!")

    def printMovies(self)->None:

        for film in self.film_list:

            print(f"\"{film.getTitle()}-{film.getGenere()}-\"\n")

    def printRentMovies(self, clientID:int):

        for k, v in self.rented_films:

            if clientID == k:

                for film in v:

                    print(f"\"{film.getTitle()}-{film.getGenere()}-\"")
                

                    