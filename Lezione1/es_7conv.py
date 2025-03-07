#es 7 lez 1 flowcharts

# Progetta un algoritmo che dati 10 
# numeri forniti dall'utente,
# conta quanti sono pari e quanti dispari.

cont = 0
pari = 0
dispari = 0

while cont < 10:

    num: float = float(input("inserisci un numero: "))

    if num % 2 == 0:
        pari+=1
    else:
        dispari+=1

    cont+=1

print(f"\nI numeri pari sono: {pari}")
print()
print(f"\nI numeri pari sono: {pari}\n")