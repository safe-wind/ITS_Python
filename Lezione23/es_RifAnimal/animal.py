#CLASSE ANIMAL
#
# - Rappresenta un animale generico del rifugio

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, id:str, name:str, age_years:int, weight_kg:float ):
        super().__init__()
        self.id = id
        self.name = name
        self.age_years= age_years
        self.weight_kg= weight_kg
    #metodi astratti:
    @abstractmethod
    def species():
        pass
    @abstractmethod
    def daily_food_grams():
        pass
    #metodi concreti:
    def info(self):
        return {
            "id":self.id,
            "name":self.name,
            "age_years":self.age_years,
            "weight_kg":self.weight_kg
            }
    def bmi_like(self):
        return float(self.weight_kg/(self.age_years+1))
    #metodi get classe animal
    def id(self):
        return self.id
    def name(self):
        return self.name
    def age_years(self):
        return self.age_years
    def weight_kg(self):
        return self.weight_kg
    