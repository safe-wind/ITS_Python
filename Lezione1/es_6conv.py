#es 6 lez 1 flowcharts

#Progetta un algoritmo per calcolare 
#il fattoriale di un numero intero 
#positivo fornito dall'utente.

while True:

    num: int = int(input("Inserire un numero intero: "))

    if num % 1==0 and num > 0:
        break

    print("Il numero deve essere positivo.")

fattoriale = 1
i = 1

while i <= num:

    fattoriale = fattoriale * i
    i += 1

print(f"Il fattoriale di {num} è: {fattoriale}")

