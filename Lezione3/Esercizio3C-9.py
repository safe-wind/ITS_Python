#esercizio3C_9


cont=0

coordinate: list[int] = []

while cont < 2:

    coordinataX : int = int(input("Inserisci coordinata X: "))
    coordinate.append(coordinataX)
    cont+=1
    coordinataY : int = int(input("Inserisci coordinata Y: "))
    coordinate.append(coordinataY)
    cont+=1

coordinate_agg : tuple = tuple(coordinate)

match coordinate_agg:

    case (0,0):
        print("Il punto si trova nell'origine.")
    case (x,0):
        print("Il punto si trova sull'asse X.")
    case (0,y):
        print("Il punto si trova sull'asse Y.")
    case coordinate_agg if coordinataX > 0 and coordinataY > 0:
        print("Il punto si trova nel primo quadrante.")
    case coordinate_agg if coordinataX < 0 and coordinataY > 0:
        print("Il punto si trova nel secondo quadrante.")
    case coordinate_agg if coordinataX < 0 and coordinataY < 0:
        print("Il punto si trova nel terzo quadrante.")
    case coordinate_agg if coordinataX > 0 and coordinataY < 0:
        print("Il punto si trova nel quarto quadrante.")
    case _:
        print("Il punto non esiste")

