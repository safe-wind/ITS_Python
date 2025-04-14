# Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a 
# number using math.sqrt(). Handle ValueError if the input is negative by returning an informative message.
from math import sqrt

def safe_sqrt(n:int) -> None:

    try:
        print(sqrt(n))
    except ValueError:
        print("ValueError: the number must be positive to calculate the square root.")

    

safe_sqrt(4)

safe_sqrt(25)
    

