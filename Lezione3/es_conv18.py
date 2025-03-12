#Scrivere un algoritmo che consenta all’utente di inserire una
#numero variabile di numeri interi (la quantità è scelta 
# dall’utente). L'algoritmo deve:

#sommare i numeri pari e maggiori della media dei numeri 
#inseriti fino a quel momento;
#sommare i numeri dispari o minori della media dei numeri 
#inseriti fino a quel momento;
#Mostrare in output entrambe le somme e indicare quale 
#somma è maggiore.

n:int=int(input("Quanti numeri vuoi inserire?: "))

i=0
sommaP = 0
sommaD = 0
somma = 0
media = 0

while i < n:

    x:int = int(input("Inserisci un numero: "))
    i+=1
    somma+=x
    media=somma/i

    if x%2 == 0 and x > media:
        sommaP += x

    if x%2 == 1 and x < media:
        sommaD += x
    

    
    

print(f"La somma dei pari è: {sommaP}\nLa somma dei dispari è: {sommaD}")

if sommaP > sommaD:
    print("La somma_pari è maggiore della somma_dispari")
elif sommaD > sommaP:
    print("La somma_dispari è maggiore della somma_pari")
else:
    print("somma_pari è uguale a somma_dispari")