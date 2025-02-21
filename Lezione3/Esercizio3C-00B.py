#ES_3C-00B

name: str = str(input("Nome: "))
genere: int = str(input("Inserire genere: m o f: "))

name = name.capitalize()

match (name, genere):

    case (name, "m"):
        print(f"{name}, Genere: Maschio")

    case (name, "f"):
        print(f"{name}, Genere: Femmina")
    
    case _:
        print(f"{name}, non è possibile generare un documento di identità")