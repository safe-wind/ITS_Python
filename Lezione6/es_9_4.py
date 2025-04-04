# Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class. Print the number of customers the restaurant has served, 
# and then change this value and print it again. Add a method called set_number_served() that lets you set the 
# number of customers that have been served. Call this method with a new number and print the value again. 
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

class Restaurant:

    def __init__(self, restaurant_name:str, cuisine_type:str) -> None:

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describeRestaurant(self) -> None:
        print(f"{self.restaurant_name}, {self.cuisine_type}")
    
    def openRestaurant(self) -> None:
        print("The restaurant is open")
    
    def numberServed(self, customer = 0) -> int:
        self.customer = customer
        return print(self.customer)
    
    def setNumberServed(self, num_serviti:int) -> int:
        self.served = num_serviti
        return print(self.served)
    
    def incrementCustomer(self) -> None:
        self.customer+=self.served
        return print(self.customer)
    

risto22 = Restaurant("Delicio", "Melting cuisine")

risto22.setNumberServed(8)
risto22.numberServed()
risto22.incrementCustomer()
        