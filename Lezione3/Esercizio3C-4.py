#esercizio3C-4

animal = input("Inserisci un animale: ")

match animal:

    case animal if animal in ["cane", "gatto", "cavallo", "elefante", "leone"]:

        print(f"{animal} appartiene alla categoria dei mammiferi")
    
    case animal if animal in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:

        print(f"{animal} appartiene alla categoria dei rettili")
    
    case animal if animal in ["aquila", "pappagallo", "gufo", "falco"]:

        print(f"{animal} appartiene alla categoria degli uccelli")
    
    case animal if animal in ["squalo", "trota", "salmone", "carpa"]:

        print(f"{animal} appartiene alla categoria dei pesci")
    
    case _:

        print(f"Non so dire in quale categoria classificare l'animale {animal}")
    