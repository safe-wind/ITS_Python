#es 8_7

def makeAlbum(name:str, album:str, songs=None) -> dict[str,str,None]:

    albumDict:dict[str, str] = {}

    if songs == None:
        albumDict:dict[str, str] = {"nome":name, "album":album}
    else:
        albumDict:dict[str, str] = {"nome":name, "album":album, "songs":songs}

    return albumDict
    
    

print(makeAlbum("Tony","GG"))
print(makeAlbum("Marvin","Sunny"))
print(makeAlbum("Plaza","Sottovuoto"))
print(makeAlbum("50 Cent","21 Questions", "8"))


            


