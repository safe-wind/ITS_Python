#es_6_7

people_list:list = list()

while True:
    first_name:str = input("Insert first name: ")
    last_name:str = input("Insert last name: ")
    age:int =(input("Insert age: "))
    city:str = (input(f"Insert city: "))
    break

person: dict = {
    "first_name": first_name,
    "last_name" : last_name,
    "age": age,
    "city": city
    }

while True:
    first_name1:str = input("Insert first name: ")
    last_name1:str = input("Insert last name: ")
    age1:int =(input("Insert age: "))
    city1:str = (input(f"Insert city: "))
    break
    
person1: dict = {
    "first_name": first_name1,
    "last_name" : last_name1,
    "age": age1,
    "city": city1
    }

while True:
    first_name2:str = input("Insert first name: ")
    last_name2:str = input("Insert last name: ")
    age2:int =(input("Insert age: "))
    city2:str = (input(f"Insert city: "))
    break
    
person2: dict = {
    "first_name": first_name2,
    "last_name" : last_name2,
    "age": age2,
    "city": city2
    }


people_list.append(person)
people_list.append(person1)
people_list.append(person2)

for x in people_list:

    for k, v in x.items():

        print(f"{k}: {v}")

    print()
        
