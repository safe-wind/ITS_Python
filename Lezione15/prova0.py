

# file = open("exemple.txt", "a")
# print(file) 
# file.close()

with open("exemple.txt", "r+") as file:
    print(file.read())  # dopo aver aperto il file WITH lo chiude automaticamente