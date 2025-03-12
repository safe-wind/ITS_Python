#Progettare un algoritmo che chieda all’utente di inserire un
#valore intero n. L'algoritmo deve:

# Verificare se n è compreso tra 1 e 100:
# se sì, calcolare e mostrare la somma di tutti i numeri pari 
# compresi tra 1 e n.
# Verificare se n è 0 o negativo:
# Se sì, mostrare un messaggio di errore e terminare.
# Altrimenti, calcolare e mostrare la somma di tutti i numeri 
# dispari compresi tra 1 e n.

n:int = int(input("Inserisci un numero intero positivo "))

if n>=1 and n<=100:
    sommaP = 0
    i_par=0

    while i_par<n:
        if i_par%2==0:
            sommaP+=i_par
        i_par+=1

    sommaD = 0
    i_dis = 0

    while i_dis < n:
        if i_dis%2==1:
            sommaD+=i_dis
        i_dis+=1

    print(f"Somma dei pari: {sommaP}\nSomma dei dispari: {sommaD}")


if n<0 or n==0:
    print("Errore")


