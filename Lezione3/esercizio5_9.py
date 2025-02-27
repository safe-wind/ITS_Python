#esercizio5_9

list_name = ["admin", "Luca", "Sofia", "Chiara"]

while len(list_name)> 0:
    list_name.pop()


if len(list_name) == 0:
    print("we need to fine users!")


for name in list_name:

    if name == "admin":
        print(f"Hello {name}! would you like to see a status report?")
    else:
        print(f"Hello {name}! thank you for logging in again")