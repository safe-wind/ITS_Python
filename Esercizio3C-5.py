#Esercizio3C-5

ruolo: str = str(input("Inserisci il tuo ruolo: "))

nome: str = str(input("Inserisci il tuo nome: "))

eta: int = int(input("Inserisci la tua eta: "))

utente: dict = {"name": nome, "age": eta, "role": ruolo}


match utente:

    case {"name": nome, "age": eta, "role": "admin"}:

        print("Accesso completo a tutte le funzionalità.")

    case {"name": nome, "age": eta, "role": "moderatore"}:

        print("Può gestire i contenuti ma non modificare le impostazioni.")
    
    case {"name": nome, "age": eta, "role": "utente"} if eta >=18:

        print("Accesso standard a tutti i servizi.")

    case {"name": nome, "age": eta, "role": "utente"} if eta < 18:

        print("Accesso limitato! Alcune funzionalità sono bloccate.")

    case {"name": nome, "age": eta, "role": "ospite"}:

        print("Accesso completo a tutte le funzionalità.")

    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")

    
    

