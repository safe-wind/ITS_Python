
class MovieCatalog:
    '''
    Attributi della classe:
    self.catalog: dict[str,lst]
    '''
    def __init__(self) -> None:
        self.setCatalog()
    #metodo per memorizzare i dettagli del catalogo

    def __str__(self) -> str:
        stringa:str = "Catalogo:"
        if self.catalog:
            for k, v in self.catalog.items():
                temp_string:str = "\n"+str(k)+": "+str(v)
                stringa += temp_string
            
        return stringa

    def setCatalog(self) -> None:

        self.catalog = {}
        
    def getCatalog(self) -> dict[str,list[str]]:
        return self.catalog
    #metodi classe MovieCatalog
    
    def add_movies(self, director_name:str, movies:list[str]) ->None:
        if not director_name:
            print("Il registra non è valido")
        elif not movies:
            print("Il film non è valido")
        # se i dati sono validi 
        else:
            # se il  regista è presente nel catalogo
            if director_name in self.catalog:
                for movie in movies:
                    #controllo se il film movie sia stato aggiunto al catalogo
                    if movie in self.catalog[director_name]:
                        print(f"Il film {movie} è già presente nel catalogo")
                    #se il film non è presente
                    else:
                        self.catalog[director_name].append(movie)
            # se il regista non è presente nel catalogo
            else:
                #creare un nuovo record
                self.catalog[director_name] = movies

    def remove_movie(self, director_name:str, movie:str) ->None:

        if not director_name:
            print("Il registra non è valido")
        elif not movie:
            print("Il film non è valido")
        # se i dati sono validi 
        else:
            if director_name in self.catalog and movie in self.catalog[director_name]:
                self.catalog[director_name].remove(movie)

            if not self.catalog[director_name]:
                del self.catalog[director_name]
    
    def list_directors(self) -> list[str] | str:
        if self.catalog:
            return list(self.catalog.keys())
        else:
            return "Non ci sono registi"
    
    def get_movies_by_director(self, director_name:str) -> list[str] | str:
        if not director_name:
            return "No director"
        else:
            if director_name in self.catalog:
                return self.catalog[director_name]
            else:
                return f"Il regista {director_name} non è nel catalogo"
            

    #def search_movies_by_title(self, title:str)
            
                


    
    