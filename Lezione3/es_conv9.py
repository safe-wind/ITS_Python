# Progettare un algoritmo che richieda 
# all’utente di inserire un valore intero 
# positivo n. Se nè negativo, il programma 
# termina mostrando un messaggio di errore. 
# Se n è positivo:

# l’utente può inserire 10 numeri interi;
# contare quanti di questi numeri sono 
# divisibili per n.
# Mostrare in output il risultato del 
# conteggio.

n:int = int(input("Inserisci un numero intero positivo: "))

if n < 0:
    print("Errore: il numero deve essere positivo")

else:
    cont = 0
    i = 0

    while True:

        x:int = int(input("Inserisci numero intero: "))
        
        if x%n == 0:
            cont+=1   
        i+=1

        if i == 10:
            print(f"{cont} numeri sono divisibili per n")
            break
        