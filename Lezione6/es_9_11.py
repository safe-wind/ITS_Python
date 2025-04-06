# Create a module users.py containing three classes:

# User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
# Privileges: holds a list of privileges and a method show_privileges() to display them.
# Admin: stores a User instance and a Privileges instance as attributes.
# In a separate file main.py, import the classes, create a User and a Privileges instance, 
# pass them to Admin, and call describe_user() and show_privileges() to verify everything works correctly.

from users import *


user1 = User("Alice", "Johnson", "alicej", "alice@example.com")

privileges1 = Privileges([
    "can add post",
    "can delete post",
    "can ban user",
    "can reset passwords"
])

admin1 = Admin(user1, privileges1)

admin1.user.describe_user()
admin1.privileges.show_privileges()