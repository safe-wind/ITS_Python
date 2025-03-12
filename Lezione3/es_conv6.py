#Progettare un algoritmo che chieda all'utente
#  di inserire un valore x positivo. Se x è
#  negativo, l'algoritmo mostra un messaggio 
# di errore e termina. Se x  è positivo, il 
# programma deve consentire all'utente di 
# inserire 10 numeri sia positivi che negativi:

# se x è pari, allora dei numeri inseriti devono
#  essere sommati solamente i numeri che sono
#  maggiori della metà di x. 
# se, invece, x è dispari, dei numeri inseriti
#  devono essere sommati solo i numeri che sono
#  minori di x. 

num_x:int = int(input("Inserisici un numero intero positivo:"))

if num_x < 0:
    print("Errore: rispetta le condizioni.")
    quit()

else:
    i = 1
    somma = 0
    
    while True:

        num:float = float(input("Inserisci numeri positivi o negativi: "))
        
        if i == 10:
            print("Programma terminato")
            break

        else:
            if num_x % 2 == 0:
                if num > (num_x/2):
                    somma +=  num
            if num_x % 2 == 1:
                if num < num_x:
                    somma += num
        i+=1

print(f"somma per x paro: {somma}")
print(f"somma per x disparo: {somma}")






