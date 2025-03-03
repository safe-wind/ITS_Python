#es_1

a: int = int(input("Inserisici l' ipotenusa a: "))
b: int = int(input("Inserisici il cateto b: "))

# a e b positivi
if a > 0 and b > 0 :

    # controllo ipotenusa maggiore del cateto
    if a > b:

        #se le condiz. sono rispettate allora:
        c = (a**2 - b**2)**(1/2)
        print(int(c))

        #altrimenti:
    else:
        print("Errore")