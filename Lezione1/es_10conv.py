#es 10

# Progettare un algoritmo che, richiesto allo 
# studente il reddito familiare e la media dei voti,
# se il reddito è inferiore a 20.000 € e la media è 
# superiore a 27 approva la borsa di studio, 
# altrimenti rifiuta la richiesta visualizzando 
# il messaggio "Borsa di studio rifiutata. "
# "(Motivo: reddito o media insufficiente)".

reddito: int = int(input("Inserisci reddito: "))
media: int = int(input("Inserisci la media: "))

if reddito > 20000 and media > 27:
    print("Richiesta borsa di studio approvata")
else:
    print("Borsa di studio rifiutata. (Motivo: reddito o media insufficiente)")
