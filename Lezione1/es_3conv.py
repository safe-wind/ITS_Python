#es_3

cont = 5
somma = 0

while cont != 0:
    num: float = float(input("Inserisci un numero: "))
   
    if num > 0:

        somma+=num
    
    else:
        cont -= 1
        continue

    cont -= 1

print(f"La somma è: {somma}")
    