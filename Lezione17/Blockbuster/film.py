
class Film:

    _id:int
    _title:str

    def __init__(self, id:int, title:str) -> None:
        self.setID(id)
        self.setTitle(title)

    def setID(self, id:int) -> None:
        self._id = id

    def setTitle(self, title:str) -> None:
        self._title = title

    def getID(self)->int:
        return self._id
    
    def getTitle(self)->str:
        return self._title
    
    # def __hash__(self):
    #     return hash(self.getID(), self.getTitle())
    
    # def __eq__(self, otherFilm)-> bool:
    #     return (self.__hash__() and otherFilm.__hash__())
    
    
    def isEqual(self, otherFilm)-> bool:

        if (self.getID(), self.getTitle()) == (otherFilm.getID(), otherFilm.getTitle()):
            return True
        else:
            return False
    


