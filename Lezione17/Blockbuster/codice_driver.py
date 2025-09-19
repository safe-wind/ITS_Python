from genere import Azione, Commedia, Drama
from noleggio import Noleggio
from film import Film



f1 = Azione(1, "Die Hard")
f2 = Azione(2, "Mad Max")
f3 = Azione(3, "John Wick")
f4 = Azione(4, "Terminator")
f5 = Azione(5, "Rambo")

f6 = Commedia(6, "Una notte da leoni")
f7 = Commedia(7, "Mr Bean")
f8 = Commedia(8, "La vita è bella")
f9 = Commedia(9, "Scary Movie")

f10 = Drama(10, "Il miglio verde")

film_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]

# Creazione oggetto Noleggio
noleggio = Noleggio(film_list)

print("Quale film vuoi nolleggiare?\n")

# Primo cliente noleggia un film
noleggio.rentAMovie(f1, 101)  # Die Hard
# Primo cliente noleggia un altro film
noleggio.rentAMovie(f2, 101)  # Mad Max
# Secondo cliente prova a noleggiare un film già preso (Mad Max)
noleggio.rentAMovie(f2, 102)
# Secondo cliente noleggia un altro film
noleggio.rentAMovie(f3, 102)  # John Wick
# Primo cliente restituisce un film (con 3 giorni di ritardo)
noleggio.giveBack(f2, 101, 3)
# Stampa film disponibili
noleggio.printMovies()
