#Progetta un algoritmo che gestisca l'iscrizione degli studenti a corsi 
# disponibili in una università. Per ogni corso ci sono un massimo di 100
#  posti liberi. Richiesto il nome del corso, mostra un menu con le seguenti
#  opzioni "iscrivi", "annulla", "visualizza", "elimina", ed "Esci". 
# Per ogni opzione:

# se l'utente inserisce "iscrivi", verifica se ci sono posti disponibili 
# per il corso, quindi incrementa il numero di posti occupati;
# se l'utente inserisce "annulla", decrementa il numero di posti occupati;
# se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il 
# numero dei posti occupati nel corso;
# se l'utente inserisce "elimina", elimina il corso e richiedi un nuovo corso;
# se l'utente inserisce "esci", termina l'algoritmo.

posti_occupati:int = 0
posti_liberi:int = 10

corso:str = str(input("Scegli un corso: "))

while True:
    
    opzione:str = str(input(f"Scegli un opzione: \"iscrivi\"|\"annulla\"|\"visualizza\"|\"elimina\"|\"esci\" (esci per uscire): "))

    if opzione == "iscrivi":
        posti_occupati+=1
        posti_liberi-=1

    if opzione == "annulla":
        posti_occupati -=1
        posti_liberi +=1

    if opzione == "visualizza":
        print(f"Nel corso di {corso} ci sono {posti_liberi} posti disponibili"
              f" e {posti_occupati} posti occupati")
    if opzione == "elimina":
        corso:str = str(input("Scegli un corso: "))
        posti_occupati:int = 0
        posti_liberi:int = 10
        
    if opzione == "esci":
        print("grazie e arrivederci!")
        break