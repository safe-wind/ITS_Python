#  Extend the LotteryMachine class you created in Exercise 9-14.

# 1. Add a method called simulate_until_win(self, my_ticket) that:

# Accepts a ticket (a list of 4 items).
# Repeatedly draws random tickets using the draw_ticket() method.
# Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
# Returns the number of attempts and the winning ticket.
# 2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

# 3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

# 4. Print a message showing:

# Your ticket
# The winning ticket
# How many attempts it took to win

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

    def simulateUntilWin(self, winning_ticket):
        attempts = 0
        while True:
            self.selectRandom()
            
            if self.winning_ticket != winning_ticket:
                attempts +=1
            else:
                print(f"You win in {attempts} attempts")
                break

lottery1 = LotteryMachine()

lottery1.selectRandom()
lottery1.displayItems()
print(f"The winning ticket: {lottery1.winning_ticket}")
lottery1.simulateUntilWin(lottery1.winning_ticket)