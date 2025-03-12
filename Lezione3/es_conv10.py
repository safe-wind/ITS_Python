#es 10 block 2
while True:
    eta:int = int(input("Inserisci l'età (\"0\" per uscire): "))
    
    if eta == 0:
        print("Programma terminato")
        break
    
    elif eta >= 18 and eta <= 65:
        print("Puoi partecipare all' attività")

    elif eta < 18:
        print("Non puoi partecipare all' attività perchè non hai raggiunto l'età minima richiesta")
    else:
        print("Non puoi partecipare all' attività perchè hai superato l'età massima consentita")