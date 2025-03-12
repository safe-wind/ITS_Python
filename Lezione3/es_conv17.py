# Sviluppare un algoritmo che chieda all’utente di inserire 7 
# temperature (una per ogni giorno della settimana). 
# L'algoritmo deve:
# calcolare la temperatura media,
# controllare se tutte le temperature sono comprese tra 10 e 30:
# Se sì, mostrare “Temperatura nella norma”.
# verificare se almeno una temperatura è maggiore di 35 o 
# minore di 5: Se sì, mostrare “Allerta temperatura”.

t_max = -100
day_max = 0
t_min = 100
day_min = 0
cont_norma = 0
t_media = 0
i=1

while True:

    temp:int = int(input("Inserisci temperatura: "))
    t_media+=temp

    if temp > t_max:
        t_max = temp
        day_max = i
    if temp < t_min:
        t_min = temp
        day_min = i
    
    if temp >= 10 and temp <= 30:
        cont_norma+=1
        if cont_norma==7:
            print("Temperature nella norma")
    elif temp < 5 or temp > 35:
        print("Allerta temperatura")
    
    i+=1
    
    
    if i>7:

        match day_max:

            case 1:
                day_max="Lunedì"
            case 2:
                day_max="Martedì"
            case 3:
                day_max="Mercoledì"
            case 4:
                day_max="Giovedì"
            case 5:
                day_max="Venerdì"
            case 6:
                day_max="Sabato"
            case 7:
                day_max="Domenica"
            case _:
                pass
    

        match day_min:

            case 1:
                day_min="Lunedì"
            case 2:
                day_min="Martedì"
            case 3:
                day_min="Mercoledì"
            case 4:
                day_min="Giovedì"
            case 5:
                day_min="Venerdì"
            case 6:
                day_min="Sabato"
            case 7:
                day_min="Domenica"
            case _:
                pass

        t_media =t_media/i
        
        print(f"temperatura media: {t_media} C°\ntemperatura massima: {t_max} C°"
              f"\ntemperatura minima: {t_min} C°\ngiorno temperatura più alta: {day_max}"
              f"\ngiorno temperatura più bassa {day_min}")
        break
        