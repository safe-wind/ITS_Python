# Lavorare con lunghezze fisse e caratteri misti.

# Esercizio 4.1: Definisci una RegEx per un CAP italiano (esattamente 5 cifre).
# Esercizio 4.2: Scrivi una RegEx che riconosca un codice fiscale italiano semplificato: 
# 6 lettere, 2 numeri, 1 lettera, 2 numeri.

#esercizio 4.1
[0-9]{5}
#esercizio 4.2
[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}
