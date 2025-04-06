# Make a class called User. Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user. 
# Create several instances representing different users, and call both methods for each user.

class User:

    def __init__(self, first_name:str, last_name:str, *args) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.user_att = args

    def describeUser(self) -> None:
        if self.user_att:
            print(f"User information: {self.first_name}, {self.last_name},", ', '.join(self.user_att))
        else:
            print(f"User information: {self.first_name}, {self.last_name}")
    def greetUser(self) -> None:
        print(f"Hi {self.first_name}, great day today")


u1 = User("Sara", "Polo", "186cm", "Capelli biondi")
u2 = User("Franciso", "San")
u3 = User("Paolo", "Polo", "168cm", "Capelli rossi")
u4 = User("Marco", "Polo", "186cm", "Capelli neri")

u2.describeUser()
u4.describeUser()