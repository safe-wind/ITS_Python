# Lavorare con formati numerici separati da caratteri speciali.

# Esercizio 5.1: Scrivi una RegEx che riconosca una data nel formato gg/mm/aaaa (es. 09/04/2025).
# Esercizio 5.2: Adatta la RegEx per accettare anche il formato gg-mm-aaaa.

#esercizio 5.1
[0-9]{2}/[0-9]{2}/[0-9]{4}
#esercizio 5.2
[0-9]{2}-[0-9]{2}-[0-9]{4}
