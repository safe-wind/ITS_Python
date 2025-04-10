# Definire pattern per email.

    # Esercizio 3.1: Scrivi una RegEx che riconosca email del tipo nome@dominio.com.
    # Esercizio 3.2: Estendi la RegEx per accettare anche domini con più estensioni, es. nome@dominio.co.uk.

#esercizio 3.1
\S+@\S+
#esercizio 3.2
\W+@[a-z]+^.$[a-z]{2}\.[a-z]{2}
