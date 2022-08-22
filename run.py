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

    def __init__(self, name, difficulty):
        self.name = name
        self.boredom = 0
        self.dirtiness = 0
        self.hunger = 0
        self.tiredness = 0

        self.foodStock = 1
        self.isAlive = True
        self.game_difficulty = self.game_level(difficulty)

    def eat(self):
        """Deduct 1 from foodStock to lower hunger"""
        if self.foodStock > 0:
            self.foodStock -= 1
            dish = random.randint(2,4)
            self.hunger -= dish
            print(f"{name} ate something from the fridge worth {dish} hunger points!")
        else:
            print(f"Fridge is empty. Go and find some food already.")

    def play(self):
        game_value = random.randint(1,4)
        if self.boredom < game_value:
            self.boredom = 0
        else:
            self.boredom -= game_value
        print(f"{name} had fun playing with you! ({game_value})")

    def sleep(self):
        self.tiredness = 0
        print(f"{name} hit the bunk! Good night, sleep tight!")

    def foodHunting(self):
        food_found = random.randint(1,3)
        self.foodStock += food_found
        print(f"{name} found {food_found} food. That will keep him going for awhile")


    def bath(self):
        bath_value = random.randint(1,4)
        if self.dirtiness < bath_value:
            self.dirtiness = 0
        else:
            self.dirtiness -= bath_value
        print(f"{name} finally took a bath! It was worth {bath_value} points!")

    def time_passed(self):
        # pet_attributes = ['boredom', 'hunger', 'dirtiness','tiredness']
        pet_attributes = [self.tiredness, self.hunger, self.boredom, self.dirtiness]
        for attr in pet_attributes:
            attr += random.randint(1, self.game_difficulty)

    def game_level:
        if level == 'easy':
            return 2
        elif level == 'medium':
            return 3
        elif level == 'hard':
            return 4
        else:
            # Don't mess with me.
            return 9999