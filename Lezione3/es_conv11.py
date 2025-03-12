#Progettare un algoritmo che richieda all’utente di inserire un valore intero.
# Il programma deve verificare: se il numero è pari e maggiore di 10. 
# Se sì, mostrare “Numero valido”;
# se il numero è dispari o minore o uguale a 10. Se sì, mostrare “Numero non valido”.

n:int = int(input("Inserisci un valore intero: "))

if n%2 == 0 and n > 10:
    print(f"Numero valido")
else:
    print(f"Numero non valido")