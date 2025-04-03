



from random import randint

tartaruga=1
lepre = 1


def mostra_posizioni(tartaruga, lepre):
    tabellone = ['_'] * 70 

    pos_tartaruga = min(tartaruga, 70)
    pos_lepre = min(lepre, 70)

    if pos_tartaruga == pos_lepre:
        tabellone[pos_tartaruga-1] = 'OUCH!!!'

    else:
        tabellone[pos_tartaruga-1] = 'T'
        tabellone[pos_lepre-1] = 'H'

    print(''.join(tabellone))

def muovi_tartaruga(tartaruga):
    mossa = randint(1, 10)

    if 1 <= mossa <= 5:
        tartaruga += 3  # Passo veloce
    
    if 6 <= mossa <= 7:
        tartaruga -= 6  # Scivolata
        if tartaruga < 1:
            tartaruga=1
    
    if 8 <= mossa <= 10 :
        tartaruga += 1 # Passo lento

    return tartaruga
        
def muovi_lepre(lepre):
    mossa = randint(1, 10)

    if 1 <= mossa <= 2:
        lepre += 0  # Riposo
        
    elif 3 <= mossa <= 4 :
        lepre += 9  # Grande balzo
        
    elif mossa == 5 :
        lepre -= 12 # Grande scivolata
        if lepre < 1:
            lepre = 1

    elif 6 <= mossa <= 8 :
        lepre += 1  # Piccolo balzo

    elif 9 <= mossa <= 10 :
        lepre -= 2  # Piccola scivolata
        if lepre < 1:
            lepre = 1
    return lepre



print("BANG !!!!!")
print("AND THEY'RE OFF !!!!!")

while tartaruga < 70 and lepre < 70:
    
    tartaruga = muovi_tartaruga(tartaruga)  # Aggiorno posizione tartaruga
    lepre = muovi_lepre(lepre)  # Aggiorno posizione lepre
    
    mostra_posizioni(tartaruga, lepre)

    if tartaruga >= 70 or lepre >= 70:
        if tartaruga >= 70 and lepre >= 70:
            print("It's a tie.")
        elif tartaruga >= 70:
            print("TORTOISE WINS! || YAY!!!")
        elif lepre >= 70:
            print("Hare wins. Yuch.")
        break