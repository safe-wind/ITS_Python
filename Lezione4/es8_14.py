#Write a function that stores information about a car in a dictionary. The function should always receive a 
# manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function 
# with the required information and two other name-value pairs, such as a color or an optional feature. Your function 
# should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the 
# dictionary that’s returned to make sure all the information was stored correctly. 

def make_car(Manufacturer:str, Model:str, **kwargs) -> str:

    output:str = f"{Manufacturer} {Model}, "
    counter = 0

    for k, v in kwargs.items():

        output += f"{k} {v}"

        if counter < len(kwargs)-1:
            output += ", "
        else:
            output += "."
        counter +=1

    return output


car  = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
