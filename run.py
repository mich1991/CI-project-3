# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import inquirer
import random

difficulty = ['easy', 'medium', 'hard']
level = inquirer.list_input('Choose difficulty level', choices=difficulty)

name = inquirer.text(message="Enter your pymagotchi name")

print(f"game difficulty is {level} and pet name is {name}")

class Pet():
    """Create a pymagotchi"""

    def __init__(self, name):
        self.name = name
        self.boredom = 0
        self.dirtiness = 0
        self.hunger = 0
        self.tiredness = 0

        self.foodStock = 1
        self.isAlive = True

    def eat(self):
        """Deduct 1 from foodStock to lower hunger"""
        if self.foodStock > 0:
            self.foodStock -= 1
            dish = random.randint(2,5)
            self.hunger -= dish
            print(f"{name} ate something from the fridge worth {dish} hunger points!")
        else:
            print(f"Fridge is empty. Go and find some food already.")


    def play(self):

    def sleep(self):

    def foodHunting(self):

    def bath(self):

