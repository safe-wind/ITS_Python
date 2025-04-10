# Unire lettere, numeri e caratteri speciali.

# Esercizio 6.1: Scrivi una RegEx per identificare un codice prodotto nel formato PROD-1234-XY.
# Esercizio 6.2: Crea una RegEx per un ID alfanumerico di esattamente 8 caratteri, che può contenere 
# lettere maiuscole e numeri (es. AB12CD34).

#esercizio 6.1
[A-Z]{4}-?[0-9]{4}-?[A-Z]{2}
#esercizio 6.2
[0-9A-Z]{8}