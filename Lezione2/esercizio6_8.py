#es6_8

pet1: dict = {
    "Turtle":"Sprinter"
}

pet2: dict = {
    "Panda":"Shifu"
}

pet3: dict = {
    "Dog":"Shaggy"
}

pet4: dict = {
    "Cat":"Cleo"
}

pets: list = [pet1, pet2, pet3, pet4]

c=0
lenght= int(len(pets))

if c<lenght:

    for i in pets:

        for k,v in i.items():

            print(f"The {k}'s owner is {v}")

        c+=1  

