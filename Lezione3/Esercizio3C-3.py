#es_3C-3

oggetti: list = []

i=0
contatore_ogg=3

while i < 3:
   oggetti.append(input(f"Inserisci {contatore_ogg} oggetti diversi: "))

   i += 1 
   contatore_ogg -= 1

print(oggetti)

match oggetti:

    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")
