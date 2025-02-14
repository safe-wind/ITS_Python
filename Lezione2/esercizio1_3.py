#es1_3

i = 0
somma = 0

while True:

    if i < 3:
        x: int = int(input("Inserisci un numero: "))
        somma=somma+x
        i+=1
        
    else:
        media = somma/i    
        print(f"La media è: {media}")
        break
