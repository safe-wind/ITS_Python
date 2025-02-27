cities: dict = {
    "Delhi": {
        "country": "India",
        "population": "33,807,400 people",
        "fact":"In the 1950, the population was 1,369,370."
    } ,
    "Roma": {
        "country":"Italy",
        "population":"4,222,631 people",
        "fact":"Rome is 2,778 years old"
    } ,
    "New York": {
        "country": "United States of America",
        "population": "7,936,530 people",
        "fact":"New York is a melting pot for different nationalities, religions and languages"
    } ,
}

cities_add: dict = {
    "Nairobi" : {"country": "Kenya",
        "population": "5,767,000 people",
        "fact":"Nairobi's population have to face with a social divide."}
}
    
cities.update(cities_add)
#print(cities)

count=0

for key, val in cities.items():

    for value in val.values():

        print(f"{key}: {value}\n", end="")


#end