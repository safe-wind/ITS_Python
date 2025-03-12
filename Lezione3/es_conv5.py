# Progettare un algoritmo che, dato un numero intero positivo n 
# definito dall'utente, 
# calcoli la somma :

# 1**2 + 2**2 + 3**2 + n**2...

# mostrando in output il risultato. Se n è negativo, 
# l'algoritmo mostra un messaggio di errore e termina. 

num:int = int(input("Inserisci un numero di vui vuoi calcolare il fattoriale: "))
somma= 0
for i in range(1, num+1):

    somma+=i**2
    
    i+=1


print(f"La somma di {num} è: {somma}")
