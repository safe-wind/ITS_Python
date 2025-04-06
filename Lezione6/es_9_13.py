# Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() 
# that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:

    def __init__(self, sides:int = 6, times=10):
        self.sides = sides
        self.times = times

    def roll_die(self):
        turno = 1
        for _ in range(self.times):
            print(f"{turno}.face of die: {randint(1,self.sides)}")
            turno += 1


die1 = Die()

print(f"die1:"), die1.roll_die()

die2 = Die(sides=10)
print(f"die2:"), die2.roll_die()

die3 = Die(sides=20)
print("die3:"), die3.roll_die()