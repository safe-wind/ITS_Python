# Add an attribute called login_attempts to your User class from Exercise 9-3. 
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, 
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

class User:

    def __init__(self, first_name:str, last_name:str, login_attempts:int, *args) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.user_att = args
        self.login_attempts = login_attempts
    
    def __str__(self) -> str:
        return f"Login attempts: {self.login_attempts}"


    def describeUser(self) -> None:
        if self.user_att:
            print(f"User information: {self.first_name}, {self.last_name},", ', '.join(self.user_att))
        else:
            print(f"User information: {self.first_name}, {self.last_name}")

    def greetUser(self) -> None:
        print(f"Hi {self.first_name}, great day today")

    def incrementLoginAttempts(self) -> int:
        self.login_attempts += 1
        return self.login_attempts
    
    def resetLoginAttempts(self) -> int:
        self.login_attempts = 0
        return self.login_attempts
    
user1 = User("Franco", "Gian", 0)

user1.incrementLoginAttempts()
user1.incrementLoginAttempts()
user1.incrementLoginAttempts()

user1.resetLoginAttempts()
print(user1)

