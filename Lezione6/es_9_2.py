# Start with your class from Exercise 9-1. Create three different instances from the class, 
# and call describe_restaurant() for each instance.

class Restaurant:

    def __init__(self, restaurant_name:str, cuisine_type:str) -> None:

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describeRestaurant(self) -> None:
        print(f"{self.restaurant_name}, {self.cuisine_type}")
    
    def openRestaurant(self) -> None:
        print("The restaurant is open") 


risto1 = Restaurant("Gia Mangiat", "Napoletano")
risto2 = Restaurant("Listolante", "Cinese")
risto3 = Restaurant("Halal", "Arabo")

risto3.describeRestaurant()
risto2.describeRestaurant()
risto1.describeRestaurant()