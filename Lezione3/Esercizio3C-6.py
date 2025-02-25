#esercizio 3C-6



animal = input("Inserisci un animale: ")

habitat = input("Inserisci habitat: ")

dizionario: dict = {}

match animal:

    case animal if animal in ["cane", "gatto", "cavallo", "elefante", "leone"]:

        print(f"{animal} appartiene alla categoria dei mammiferi")
        animal_type = "mammiferi"
        dizionario_mammiferi = dizionario.update({"animale" : animal, "habitat" : habitat, "tipo" : animal_type})

        match dizionario_mammiferi:

            case {"animale": animal, "habitat": "acqua", "tipo": "mammiferi"}:
                print(f"L'animale {animal} è uno dei mammiferi che può vivere in acqua!")
            case {"animale": animal, "habitat": "terra", "tipo": "mammiferi"}:
                print(f"L'animale {animal} è uno dei mammiferi che può vivere sulla terra !")
            case _:
                print("Errore")

            
                

    
    case animal if animal in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:

        print(f"{animal} appartiene alla categoria dei rettili")
        animal_type = "rettili"
        dizionario_rettili = dizionario.update({"animale" : animal, "habitat" : habitat, "tipo" : animal_type})

        match dizionario_rettili:

            case {"animale": animal, "habitat": "acqua", "tipo": "rettili"}:
                print(f"L'animale {animal} è uno dei rettili che può vivere in acqua!")
            case {"animale": animal, "habitat": "terra", "tipo": "rettili"}:
                print(f"L'animale {animal} è uno dei rettili che può vivere sulla terra !")
            case _:
                print("Errore")


    case animal if animal in ["aquila", "pappagallo", "gufo", "falco"]:

        print(f"{animal} appartiene alla categoria degli uccelli")
        animal_type = "uccelli"
        dizionario_uccelli = dizionario.update({"animale" : animal, "habitat" : habitat, "tipo" : animal_type})

        match dizionario_uccelli:

            case {"animale": animal, "habitat": "aria", "tipo": "uccelli"}:
                print(f"L'animale {animal} è uno degli uccelli che può vivere in aria!")
            case {"animale": animal, "habitat": "terra", "tipo": "uccelli"}:
                print(f"L'animale {animal} è uno degli uccelli che può vivere sulla terra !")
            case {"animale": animal, "habitat":"acqua", "tipo":"uccelli"}:
                print(f"L'animale {animal} è uno degli uccelli che può vivere in acqua !")
            case _:
                print("Errore")
    
    case animal if animal in ["squalo", "trota", "salmone", "carpa"]:

        print(f"{animal} appartiene alla categoria dei pesci")
        animal_type = "pesci"
        dizionario_pesci = dizionario.update({"animale" : animal, "habitat" : habitat, "tipo" : animal_type})

        match dizionario_pesci:

            case {"animale": animal, "habitat":"acqua", "tipo":"pesci"}:
                print(f"L'animale {animal} è uno degli uccelli che può vivere in acqua !")
            case _:
                print("Errore")
    
    case _:

        print(f"Non so dire in quale categoria classificare l'animale {animal}")
        animal_type= "sconosciuto"


    