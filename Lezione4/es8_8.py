# es8_8

def makeAlbum(name:str, album:str, songs=None) -> dict[str,str,None]:

    albumDict:dict[str, str] = {}

    if songs == None:
        albumDict:dict[str, str] = {"nome":name, "album":album}
    else:
        albumDict:dict[str, str] = {"nome":name, "album":album, "songs":songs}

    return albumDict

while True:

    scelta=input("Vuoi inserire informazioni su un album (quit to exit | yes to continue): ")
    scelta.lower()

    if scelta == "yes":

        name:str = str(input("Inserisci artista: "))
        album:str = str(input("Inserisci album: "))
        songs:str = str(input("Sai quante canzoni sono? (0 se non lo sai): "))
        if songs == 0:
            songs==None
        else:
            continue

        print(makeAlbum())

    if scelta == "quit":
        break

print(makeAlbum(name, album, songs))
    


