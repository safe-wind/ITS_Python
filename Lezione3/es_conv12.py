#Progettare un algoritmo che richieda all’utente di inserire un numero 
# variabile n di valori x e y. L'algoritmo deve:

# calcolare il prodotto di x e y solo se entrambi i valori sono positivi;
# calcolare la somma di x e y solo se uno dei due valori è negativo;
# mostrare il risultato dell’operazione effettuata o un messaggio di
# errore altrimenti.

n:int = int(input("Scegli quanti numeri inserire:"))

i=0
while True:

    x:int = int(input("Inserisci un numero x: "))
    y:int = int(input("Inserisci un numero y: "))

    if x > 0 and y > 0:
        result = x*y
        print(f"Il risultato è {result}")
        
    elif x < 0 and y < 0:
        print("Errore")
        
    else:
        result = x - abs(y)
        print(f"Il risultato è {result}")
    i += 1

    if i == n:
        print("Programma terminato")
        break
        