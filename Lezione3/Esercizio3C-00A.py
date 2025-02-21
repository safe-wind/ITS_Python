#ES_3C-00A

neonati : int = int(input("Inserisci quanti neonati: "))

match neonati:

    case 1:
        print("Congratulazioni!")
    case 2:
        print("WOW! Gemelli!")
    case 3:
        print("WOW! Tre!")
    case 4 :
        print("Mamma mia quattro!")
    case 5 :
        print("Incredibile! Cinque!")
    case _:
        print(f"Non ci credo! {neonati} bambini!")