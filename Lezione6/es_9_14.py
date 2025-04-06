# Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. 
# Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. 
# Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.

import random

class LotteryMachine:

    def __init__(self) -> None:
        self.items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
        self.winning_ticket = []

    def selectRandom(self):
        
        self.winning_ticket = random.choices(self.items, k=4)

    def displayItems(self):
        print("Winning Ticket:", self.winning_ticket)
        print("Any ticket matching these 4 items wins a prize!")

        

lottery1 = LotteryMachine()

lottery1.selectRandom()
lottery1.displayItems()