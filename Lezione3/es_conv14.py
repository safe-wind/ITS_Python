# Progettare un algoritmo che simuli un gioco basato sul lancio
# di due dadi virtuali a sei facce, D1 e D2. L'algoritmo deve
# eseguire le seguenti operazioni:

# Simulare il lancio dei due dadi.
# Calcolare la somma dei valori ottenuti dai due dadi.
# Applicare le seguenti regole di gioco per determinare 
# il punteggio: Se entrambi i dadi mostrano numeri pari e 
# la somma è maggiore di 8, il giocatore vince e il punteggio 
# è impostato direttamente a 100. Se uno dei dadi mostra 6 
# oppure la somma è uguale a 7, il punteggio del giocatore 
# viene incrementato di 10. In tutti gli altri casi, il 
# giocatore perde e il punteggio è impostato a 0.
# Mostrare il risultato del gioco e il punteggio ottenuto.
# Il gioco continua finché il punteggio totale del giocatore 
# non raggiunge 100 (vittoria) oppure scende a zero

punteggio = 0

d1:int = int(input("DADO 1: Inserisci un numero compreso tra 1 e 6: "))
d2:int = int(input("DADO 2: Inserisci un numero compreso tra 1 e 6: "))

if d1>0 and d1<=6:

    if d2>0 and d2<=6:
        somma=d1+d2

if d1%2==0 and d2%2==0 and somma>8:
    punteggio = 100
    
elif d1==6 or d2==6 or somma==7:
    punteggio+=10

else:
    punteggio=0

if punteggio>=100 or punteggio==0:
        if punteggio >= 100:
            print("Vittoria")
            quit()
            
        elif punteggio == 0:
            print("Sconfitta")
            quit()
            
    
while punteggio>=100 or punteggio>0:

    d1:int = int(input("DADO 1: Inserisci un numero compreso tra 1 e 6: "))
    d2:int = int(input("DADO 2: Inserisci un numero compreso tra 1 e 6: "))
    
    if d1%2==0 and d2%2==0 and somma>8:
        punteggio = 100
    
    elif d1==6 or d2==6 or somma==7:
        punteggio+=10

    else:
        punteggio=0
        

    if punteggio>=100 or punteggio==0:
        if punteggio >= 100:
            print("Vittoria")
            break
        elif punteggio == 0:
            print("Sconfitta")
            break
    