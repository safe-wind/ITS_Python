#es_3C-1

voto : int = int(input("Inserire un voto da 1 a 10: "))

match voto:

    case voto if voto >= 1 and voto <=3:
        print("Gravemente insufficiente")
    case voto if voto >= 4 and voto <= 5:
        print("Insufficiente")
    case voto if voto >= 6 and voto <= 7:
        print("Sufficiente")
    case voto if voto >= 8 and voto <= 9:
        print("Molto buono")
    case voto if voto==10:
        print("Eccellente")
    case _:
        print("Voto non valido")