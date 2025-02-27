#es 5_10

current_users: list[str] = ["jibbo", "mical", "gabba", "frost", "heat"]

new_user : list[str] = ["jibbo", "frost", "waael", "clare", "oppo"]

for i in new_user:

    i.lower()


for loop in new_user:


    if loop in current_users:

        print(f"Username {loop}, is not avaible will need to enter a new username")
    
    else:
        print(f"The username {loop}, is avaible")

