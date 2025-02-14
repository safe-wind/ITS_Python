#es6_7

persona1: dict = {
    "first_name": "Adam", 
    "last_name": "Sandler",
    "age": 58,
    "city": "New York"
}

persona2: dict = {
    "first_name": "Ken", 
    "last_name": "Jeong",
    "age": 55,
    "city": "Detroit"
}

persona3: dict ={
    "first_name": "Myke", 
    "last_name": "Tyson",
    "age": 58,
    "city": "New York"
}
people : list = [persona1, persona2, persona3]

for i in people.__iter__():

    print(f"{i}\n")


