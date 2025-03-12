# Progettare un algoritmo che consenta all’utente di inserire 
# 10 numeri interi. L'algoritmo deve: contare quanti numeri
# sono positivi e quanti sono negativi, verificare quanti 
# numeri positivi sono pari e maggiori di 20, verificare quanti
# numeri negativi sono dispari o minori di -10.
# Mostrare in output i conteggi distinti per ogni categoria.
dispari = 0
pari = 0
negativi = 0
positivi = 0

i=0

while i!=10:

    n:int = int(input("Inserisci un numero positivo o negativo: "))

    if n%1 == 0 and n!=0:
        
        if n > 0:
            positivi+=1
            if n%2 == 0 and n > 20:
                pari+=1
        
        else:
            negativi+=1
            if n%2 != 0 or n < -10:
                dispari+=1
        i+=1
        
    else:
       n:int = int(input("Inserisci un numero positivo o negativo: "))

print(f"Positivi: {positivi}\nNegativi: {negativi}\nPari: {pari}\nDispari: {dispari}")

