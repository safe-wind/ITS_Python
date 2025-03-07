#es 7 lez 1

# Progetta un algoritmo che dati 7 numeri,
# trova e comunica i numeri maggiori di 
# un valore soglia fornito dall'utente.

soglia: float = float(input("Inserisci un valore soglia: "))

cont = 0

while cont < 7:

    num: float = float(input("Inserisci un numero: "))

    if num > soglia:
        print(f"{num} è maggiore del valore soglia")
    
    cont += 1
