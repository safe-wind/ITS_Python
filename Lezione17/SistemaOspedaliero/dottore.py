from persona import Persona

class Dottore(Persona):
    _specialization: str
    _parcel: float

    def __init__(self, nome, cognome, eta, specialization, parcel):
        super().__init__(nome, cognome, eta)
        if isinstance(specialization, str):
            self.specialization = specialization
        else:
            self.specialization = None
            print("La specializzazione inserita non è una stringa!")
        if isinstance(parcel, float):
            self.parcel = parcel
        else:
            self.parcel = None
            print("La parcella inserita non è un float!")

    def setSpecialization(self, specialization):
        if isinstance(specialization, str):
            self.specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel):
        if isinstance(parcel, float):
            self.parcel = parcel
        else:
            print("La parcella inserita non è un float!")
    def getSpecialization(self):
        return self.specialization

    def getParcel(self):
        return self.parcel

    def isAValidDoctor(self):
        if super().getAge() > 30:
            print(f"Doctor {self.nome} {self.cognome} is valid!")
            return True
        else:
            print(f"Doctor {self.nome} {self.cognome} is not valid!")
            return False

    def doctorGreet(self):
        super().greet()
        print(f"Sono un medico {self.specialization}")
        print(f"Sono un medico {self.specialization}")