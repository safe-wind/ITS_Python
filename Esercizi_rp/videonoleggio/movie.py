class Movie:

    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = False) -> None:
        self._movie_id = movie_id
        self._title = title
        self._director = director
        self._is_rented = is_rented

    def rent(self) -> None:
        if not self._is_rented:
            self._is_rented = True
        else:
            print(f"Il film {self.title} è già noleggiato")

    def return_movie(self) -> None:
        if self._is_rented:
            self._is_rented = False
        else:
            print(f"Il film {self.title} non è stato noleggiato da questo cliente")

    def __str__(self):
        stato = "no" if self._is_rented else "si"
        return f"Id: {self._movie_id}, Titolo: {self._title}, Director: {self._director}, Disponibile: {stato}"
