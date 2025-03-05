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
        songs:str = str(input("Sai quante canzoni sono? (None se non lo sai): "))
        
        print(makeAlbum(name, album, songs))

    if scelta == "quit":
        print("Programma terminato")
        break

    


