#esercizio 3C-6



animal = input("Inserisci un animale: ")

habitat = input("Inserisci habitat: ")

dizionario: dict = {}

match animal:

    case animal if animal in ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]:

        print(f"{animal} appartiene alla categoria dei mammiferi")
        animal_type = "mammiferi"
        dizionario = {"animale" : animal, "habitat" : habitat, "tipo" : animal_type}

        match dizionario:

            case animal if ["balena", "delfino"] and habitat=="acqua":
                print(f"L'animale {animal} è uno dei mammiferi che può vivere in acqua!")
            case animal if ["cane", "gatto", "cavallo", "elefante", "leone"] and habitat=="terra":
                print(f"L'animale {animal} è uno dei mammiferi che può vivere sulla terra !")
            case _:
                print("Errore")
                

    case animal if animal in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:

        print(f"{animal} appartiene alla categoria dei rettili")
        animal_type = "rettili"
        dizionario = {"animale" : animal, "habitat" : habitat, "tipo" : animal_type}

        match dizionario:

            case animal if ["coccodrillo", "tartaruga", "serpente"] and habitat=="acqua":
                print(f"L'animale {animal} è uno dei mammiferi che può vivere in acqua!")
            case animal if ["serpente", "lucertola", "tartaruga"] and habitat=="terra":
                print(f"L'animale {animal} è uno dei mammiferi che può vivere sulla terra !")
            case _:
                print("Errore")


    case animal if animal in ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]:

        print(f"{animal} appartiene alla categoria degli uccelli")
        animal_type = "uccelli"
        dizionario = dizionario.update({"animale" : animal, "habitat" : habitat, "tipo" : animal_type})

        match dizionario:

            case animal if ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra"] and habitat=="aria":
                print(f"L'animale {animal} è uno dei mammiferi che può vivere in acqua!")
            case animal if ["gallina", "tacchino"] and habitat=="terra":
                print(f"L'animale {animal} è uno dei mammiferi che può vivere sulla terra !")
            case _:
                print("Errore")
    
    case animal if animal in ["squalo", "trota", "salmone", "carpa"]:

        print(f"{animal} appartiene alla categoria dei pesci")
        animal_type = "pesci"
        dizionario = {"animale" : animal, "habitat" : habitat, "tipo" : animal_type}

        match dizionario:

            case animal if ["squalo", "trota", "salmone", "carpa"] and habitat=="acqua":
                print(f"L'animale {animal} è uno dei mammiferi che può vivere in acqua!")
            case _:
                print("Errore")
    
    
    case _:

        print(f"Non so dire in quale categoria classificare l'animale {animal}")
        animal_type= "sconosciuto"


    