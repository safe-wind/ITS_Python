#Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli
# da un parcheggio con un numero massimo di posti dato in input. L'utente 
# può inserire una delle seguenti opzioni "ingresso", "uscita", "stato", 
# "esci". Per ogni opzione:

# se l'utente inserisce "ingresso", verifica se ci sono posti disponibili, 
# quindi incrementa il numero di posti occupati;
# se l'utente inserisce "uscita", verifica che ci siano veicoli nel parcheggio,
#  quindi decrementa il numero di posti occupati;
# se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
# se l'utente inserisce "esci", termina l'algoritmo.
# Torna all'inserimento di una opzione finché l'utente non seleziona "esci".

max_posti:int = int(input("Quanti posti ci sono nel parcheggio?: "))
liberi = max_posti
occupati:int = 0

while True:

    if liberi <=max_posti and liberi > 0:

        scelta:str = str(input("Scegli un opzione: \"ingresso\"|\"uscita\""
        "|\"stato\"|\"esci\" (esci per uscire): "))

        match scelta:

            case "ingresso":
                match occupati:
                    case occupati if occupati >= 0:
                        liberi -= 1
                        occupati += 1

            case "uscita":
                match liberi:
                    case liberi if liberi < 20:
                        liberi  +=1 
                        occupati -= 1

            case "stato":
                posti_liberi = 20 - occupati
                posti_occupati = occupati
                print(f"Ci sono {posti_liberi} posti liberi, {posti_occupati} sono occupati")

            
            case "esci":
                print("Grazie e arrivederci!")
                break
            case _:
                print("Non è possibile eseguire questa azione")

    else:
        print("siamo pieni")