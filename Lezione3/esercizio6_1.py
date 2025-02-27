#es6_1



while True:

    first_name:str = input("Insert first name: ")

    last_name:str = input("Insert last name: ")

    age: str =(input("Insert age: "))

    city:tuple = (input(f"Insert city: "))

    person: dict = {
    "first_name": first_name,
    "last_name" : last_name,
    "age": age,
    "city": city
    }
    
    for k, v in person.items():

        print(f"{k}: {v}\n")
    
          