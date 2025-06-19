from movie import Movie

class Customer:

    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie] = None):
        self._customer_id = customer_id
        self._name = name
        self._rented_movies = rented_movies if rented_movies is not None else []

    def rent_movie(self, movie: Movie): 
        if not movie._is_rented:
            movie.rent()
            self._rented_movies.append(movie)
        else:
            print(f"Il film {movie.title} è già noleggiato")

    def return_movie(self, movie: Movie): 
        if movie in self._rented_movies:
            movie.return_movie()
            self._rented_movies.remove(movie)
        else:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente")

    def __str__(self):
        if self._rented_movies:
            elenco: str = ", ".join(i._title for i in self._rented_movies)
        else:
            elenco = "Nessun film noleggiato"
        return f"ID: {self._customer_id}, Nome: {self._name}, Rented Movies: {elenco}"
