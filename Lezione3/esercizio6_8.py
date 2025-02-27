#es6_8

pet1:dict = {"owner":"Lucia",
             "pet":"tortoise"
            }

pet2:dict = {"owner":"Luca",
             "pet":"dog"
            }

pet3:dict = {"owner":"Maria",
             "pet":"cat"
            }

pets: list[dict] = [pet1, pet2, pet3]

cont = 0


for dizionari in pets:
        
    for key in dizionari.keys():
                
        if  key == "owner":

            who=dizionari[key]

        elif key == "pet":

            pet=dizionari[key]

    
    print(f"{who}'s pet is a {pet}")
    print()



