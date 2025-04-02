



from random import randint
table = ["_"]*70

def percorso(mossaT:int, mossaL:int) -> list[str]:
    if mossaT == mossaL:
        print("OUCH!")
    

def tartaruga(posizione:int = 1):
    tar = "T"
    count_t = 0
    
    mossaT = randint(1, 10)
    
    if mossaT >= 1 and mossaT<=5:
        posizione += 3
    elif mossaT >= 6 and mossaT<=7:
        posizione-=6
        if posizione<1:
            posizione=1
    else:
        posizione+=1

    pass
                


def lepre(posizione:int = 1):
    lep = "L"
    count_l = 0

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
    tartaruga()
    lepre()
    break