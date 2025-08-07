

class Specie:

    def __init__(self, nome:str, popolazione:int, tasso_crescita:float):
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    def cresci(self, popolazione:int):
        popolazione *= (1+ self.tasso_crescita/100)
        return popolazione

    def anni_per_superare(self, altra_specie) -> int:
        anni = 1
        pop_self = self.popolazione
        pop_altra = altra_specie.popolazione
        while pop_self <= pop_altra and anni < 1000:
            pop_self *= (1 + self.tasso_crescita / 100)
            pop_altra *= (1 + altra_specie.tasso_crescita / 100)
            anni += 1
        return anni if pop_self > pop_altra else -1

    def getDensita(self, area_kmq: float) -> int:
        anni = 0
        pop = self.popolazione
        while pop / area_kmq < 1 and anni < 1000:
            pop *= (1 + self.tasso_crescita / 100)
            anni += 1
        return anni if pop / area_kmq >= 1 else -1
            
    
class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione_iniziale, tasso_crescita)

class Elefante(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)



# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")