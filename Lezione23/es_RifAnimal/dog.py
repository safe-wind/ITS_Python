from animal import Animal


class Dog(Animal):
    def __init__(self, id, name, age_years, weight_kg, breed:str, is_trained:bool):
        super().__init__(id, name, age_years, weight_kg)

        self.breed= breed
        self.is_trained = is_trained
    
    def species(self):
        return "dog"
    
    def daily_food_grams(self):
        return 200 + self.age_years * 50
    
    def info(self):
        data = super().info()

        data["breed"] = self.breed
        data["is_trained"] = self.is_trained
    
    