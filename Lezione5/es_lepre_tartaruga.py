# percorso = 70 quadrati
# posizione = 1 quadrato 
# traguardo = 70
# if gareggiatore >= 70 ---> WIN!

# orologio = 0

from random import randint


def percorso(mossaT:int, mossaL:int) -> list[str]:
    if mossaT == mossaL:
        print("OUCH!")
        
    percorso = ["_"]*70
    return percorso

def tartaruga(posizione:int = 1):


    while posizione < 70:
        mossaT = randint(0, 10)
        pass
                


def lepre(posizione:int = 1):

    while posizione < 70:
        mossaL = randint(1,10)
        #match mossaL:
        pass


print(percorso(mossaL=1, mossaT=1))


#gioco

while True:
    print("BANG! AND THEY'RE OFF!!")
    break