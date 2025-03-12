#Scrivere un algoritmo che calcoli il valore di una sequenza 
# numerica basata su un valore n inserito dall’utente. 
# La sequenza segue queste regole:

# se n è pari, calcolare la somma dei numeri da 1 a n che sono
#  divisibili per 4;
# se n è dispari, calcolare il prodotto dei numeri dispari da 
# 1 a n;
# se n è negativo, mostrare un messaggio di errore e terminare.

n:int = int(input("Inserire un numero: "))

if n<=0:
    print("Errore")
    quit()



if n%2==0:

    cont = 4
    result = 0
    while cont <= n:

        result += cont
        cont += 4

        if cont > n:
            print(f"Il risultato è: {result}")
            break
else:

    cont = 1
    result = 1
    while cont <= n:

        result *= cont
        cont += 2

        if cont > n:
            print(f"Il risultato è: {result}")
            break
       