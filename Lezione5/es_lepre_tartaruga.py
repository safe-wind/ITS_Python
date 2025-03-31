# percorso = 70 quadrati
# posizione = 1 quadrato 
# traguardo = 70
# if gareggiatore >= 70 ---> WIN!

# orologio = 0

from random import randint

global percorso
percorso = ["_"]*70

def percorso():
    percorso = ["_"]*70
    return percorso

def tartaruga(mossa, posizione:int = 1):

    while posizione < 70:
        mosseT = randint(0, 10)
        pass
                


def lepre(mossa, posizione:int = 1):

    mosseL = randint(0, 10)
    while posizione < 70:
        pass


print(percorso(table = [range(70)]))


#gioco

while True:
    print("BANG! AND THEY'RE OFF!!")
    break