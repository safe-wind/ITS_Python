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
        if mossaL >= 1 and mossaL<= 2:#riposo
            posizione+=0
        elif mossaL >=3 and mossaL<=4:#grande balzo
            posizione+=9
        elif mossaL==5:#grande scivolata
            posizione-=12
            if posizione < 1:
                posizione = 1
        elif mossaL >= 6 and mossaL<=8:#piccolo balzo
            posizione += 1
        else: #piccola scivolata
            posizione-=2
            if posizione < 1:
                posizione=1
    
        if posizione == 70:
            print("GAME WIN")
        count_l += 1

        


print(lepre())


#gioco

while True:
    print("BANG! AND THEY'RE OFF!!")
    break