# Create a module users.py containing three classes:

# User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
# Privileges: holds a list of privileges and a method show_privileges() to display them.
# Admin: stores a User instance and a Privileges instance as attributes.
# In a separate file main.py, import the classes, create a User and a Privileges instance, pass them to Admin, 
# and call describe_user() and show_privileges() to verify everything works correctly.


class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"User Info:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!\n")


class Privileges:
    def __init__(self, privileges:list[str]=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            print("Admin Privileges:")
            for privilege in self.privileges:
                print(f"  - {privilege}")
        else:
            print("This admin has no privileges assigned.")


class Admin:
    def __init__(self, user, privileges):
        self.user = user
        self.privileges = privileges


    






        


