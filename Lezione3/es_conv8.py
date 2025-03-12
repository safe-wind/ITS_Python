# Progettare un algoritmo che chieda all’utente di inserire 
# due valori interi positivi 𝐴 e 𝐵 con 𝐴 < 𝐵. Se i valori
#  non rispettano le condizioni, mostrare un messaggio di 
# errore e terminare. Se i valori sono validi, calcolare la 
# somma di tutti i numeri interi compresi tra 𝐴 e 𝐵 (inclusi)
#  e mostrare il risultato.

a:int = abs(int(input("Inserisci il numero A: ")))
b:int = abs(int(input("Inserisci il numero B: ")))

if a < b:
    if a > 0 and b > 0:
        if a%1 == 0 and b%1 == 0:
            somma=0
            i=a
            while i <= b:

                for iter in range(a, b +1):
                    somma += iter
                    i+=1
        else:
            print("Errore: A e B devono essere interi")
    else:
        print("Errore: A e B devono essere positivi")   
else:
    print("Errore: A deve essere minore di B ")

print(f"La somma è {somma}")

