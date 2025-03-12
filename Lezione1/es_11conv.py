# Progetta un algoritmo per gestire la prenotazione
# dei posti in una sala che contiene 20 sedie libere
# . L'utente può inserire una delle seguenti opzioni'
# ' "prenota", "libera", "visualizza", "esci". '
# 'Per ogni opzione:

# se l'utente inserisce "prenota", se ci sono ancora'
# sedie libere, decrementa di uno il numero di
# posti liberi;
# se l'utente inserisce "libera", incrementa di 
# uno il numero di sedie libere;
# se l'utente inserisce "visualizza", mostra il '
# 'numero dei posti liberi e il numero dei posti '
# 'occupati;
# se l'utente inserisce "esci", termina l'algoritmo.

# Torna all'inserimento di una opzione finché '
# 'l'utente non seleziona "esci".

liberi:int = 20
occupati:int = 0

while True:

    if liberi <=20 and liberi > 0:

        scelta:str = str(input("Scegli un opzione: \"prenota\"|\"libera\""
        "|\"visualizza\"|\"esci\" (esci per uscire): "))

        match scelta:

            case "prenota":
                match occupati:
                    case occupati if occupati >= 0:
                        liberi -= 1
                        occupati += 1

            case "libera":
                match liberi:
                    case liberi if liberi < 20:
                        liberi  +=1 

            case "visualizza":
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


