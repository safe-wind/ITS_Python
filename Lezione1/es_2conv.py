#es_2

max_val: float = float(input("Inserisci un numero: "))
cont = 1

while True:

    num: float = float(input("Inserisci un numero:"))

    if num > max_val:

        max_val = num
    
    cont += 1

    if cont == 5:
        break

print(f"Il numero maggiore della serie è: {max_val}")