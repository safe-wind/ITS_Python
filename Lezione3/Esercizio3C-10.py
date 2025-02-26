#esercizio3C-10

giorno: int = int(input("Inserisci un giorno: "))

mese: int = int(input("Inserisic un mese: "))

festivo: list[int] = [giorno, mese]

festivo:tuple= tuple(festivo)

match festivo:

    case (1,1):
        print("Capodanno")
    case (14,2):
        print("San Valentino")
    case (2,6):
        print("Festa della repubblica")
    case (15,8):
        print("Ferragosto")
    case (31,10):
        print("Halloween")
    case (25,12):
        print("Natale")
    case _:
        print("Nessuna festività importante in questa data.")
    