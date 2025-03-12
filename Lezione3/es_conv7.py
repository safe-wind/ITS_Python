#Progettare un algoritmo che consenta di inserire all'utente 
# un elenco di voti non negativi relativi ad un esame, 
# calcolandone la media. L'algoritmo deve chiedere all'utente
#  se vuole inserire un voto. 
#Se la risposta è "SI", allora l'utente può procedere ad
#  inserire il voto. L'algoritmo deve consentire all'utente 
# di inserire voti fin quando la risposta dell'utente sarà "NO". 
#Infine, mostrare in output il valore medio dei voti inseriti.

cont = 0 
somma = 0 

while True:

    scelta:str = str(input("Vuoi inserire un voto? (\"SI\"|\"NO\"): "))
    scelta = scelta.upper()

    if scelta == "SI":
    
        voto:int = int(input("Inserisci un voto: "))
        if voto > 0:
            somma+=voto
            cont+=1
        else:
            print("Errore")

    elif scelta == "NO":
        
        if cont > 0:
            media = somma/cont
            print(f"La media dei voti è: {media}")
            break
        else:
            print("Nessun voto inserito")
            break


    
