
class Media:

    def __init__(self, title:str)-> None:

        self.set_title(title)
        self.reviews:list[int] = []

    def set_title(self, title:str)-> None:
        self.title = title

    def get_title(self) -> str:
        return self.title
    
    def aggiungiValutazione(self, voto:int)->None:

        if voto not in range(1,6):
            raise ValueError("Devi inserire un voto  da 1 a 5")
        else:
            self.reviews.append(voto)
    
    def getMedia(self)-> float:
        result=0

        for elmnt in self.reviews:
            result+=elmnt
        
        media = result/(len(self.reviews))

        return media

    def getRate(self, n = None)->str:
        if n==None:
            n = self.getMedia() 

            match n:
                case n if round(n) == 1:
                    return f"Giudizio: Terribile"
                case n if round(n) == 2:
                    return f"Giudizio: Brutto"
                case n if round(n) == 3:
                    return f"Giudizio: Normale"
                case n if round(n) == 4:
                    return f"Giudizio: Bello"
                case n if round(n) == 5:
                    return f"Giudizio: Grandioso"
        else:
            match n:
                case n if round(n) == 1:
                    return f"Giudizio: Terribile"
                case n if round(n) == 2:
                    return f"Giudizio: Brutto"
                case n if round(n) == 3:
                    return f"Giudizio: Normale"
                case n if round(n) == 4:
                    return f"Giudizio: Bello"
                case n if round(n) == 5:
                    return f"Giudizio: Grandioso"
            
    def ratePercentage(self, voto:int)->str:
        #voti totali
        quantita_voti = len(self.reviews)
        #quanti voti trovati 
        conta_voto = 0

        # tutti i voti presenti
        #il voto selezionato
        #
        #
        for elmnt in self.reviews:
            if elmnt==voto:
                conta_voto+=1
        
        perc_voti = (conta_voto/quantita_voti) * (100)

        return f"{perc_voti}%"
    
    def recensione(self)-> None:
       
        print(
            f"Titolo del Film: {self.get_title()}\n"
            f"Voto medio: {self.getMedia()}\n"
            f"{self.getRate()}\n"
            f"Terribile: {self.ratePercentage(1)}\n"
            f"Brutto: {self.ratePercentage(2)}\n"
            f"Normale: {self.ratePercentage(3)}\n"
            f"Bello: {self.ratePercentage(4)}\n"
            f"Grandioso: {self.ratePercentage(5)}\n"
        )

            
class Film(Media):

    pass


if __name__ == "__main__":

    film1 = Film("The Shawshank Redemption")
    valutazioni1 = [5, 5, 5, 4, 4, 5, 5, 5, 4, 5]
    for voto in valutazioni1:
        film1.aggiungiValutazione(voto)

    film2 = Film("Inception")
    valutazioni2 = [3, 4, 4, 3, 4, 3, 2, 4, 3, 5]
    for voto in valutazioni2:
        film2.aggiungiValutazione(voto)

    film3 = Film("Twilight")
    valutazioni3 = [1, 1, 2, 2, 1, 2, 2, 1, 1, 2]
    for voto in valutazioni3:
        film3.aggiungiValutazione(voto)

    print("\n--- Recensione Film 1 ---")
    film1.recensione()

    print("\n--- Recensione Film 2 ---")
    film2.recensione()

    print("\n--- Recensione Film 3 ---")
    film3.recensione()