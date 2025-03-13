#Build a profile of yourself by calling build_profile(), 
# using your first and last names and three other key-value 
# pairs that describe you. All the values must be passed to t
# he function as parameters. The function then must return a 
# string such as 
# "Eric Crow, age 45, hair brown, weight 67"

def build_profile(first_name:str, last_name:str, **kwargs) -> str:

    output= f"{first_name} {last_name}: "
    counter = 0

    for key, value in kwargs.items():
        output += f"{key} {value}"

        if counter < len(kwargs) - 1:
            output += ", "
        else:
            output+="."
        counter += 1
        
    return output

output = build_profile("Marius", "Gidilica", age=25, hair="brown", weight=70, height="170cm")
print(output)

