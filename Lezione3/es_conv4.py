# Progettare un algoritmo che assegni i 10 
# tutor disponibili agli studenti che 
# necessitano di recupero in un istituto 
# scolastico. Per ogni studente dato in input,
# il sistema deve controllare la disponibilità
# dei tutor e, nel caso di disponibilità, 
# assegnarlo allo studente. Se il numero di 
# tutor disponibili scende a zero, occorre 
# aumentare il numero di studenti in lista 
# d'attesa. Occorre confermare sia l’assegnazione'
# ' del tutor con successo che l'inserimento
# nella lista d’attesa allo studente. 
# L'algoritmo termina solo quando il numero '
# 'di tutor è pari a 0 e la lista d'attesa 
# conta 50 studenti.

n_tutor:int = 10
attesa:int = 0


while True:

    n_studenti:int  = int(input("Inserisci quanti studenti hanno bisogno di 1 tutor: "))

    if n_tutor > 0:
        print("Tutor assegnato con successo")
        n_tutor -= n_studenti
    
    if n_tutor == 0:
        print("Studente in attesa")
        attesa += 1
    
    if  n_tutor==0 and attesa > 2:
        print("Spazio finito")
        break

    
    