# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import inquirer
import random

difficulty = ['easy', 'medium', 'hard']
level = inquirer.list_input('Choose difficulty level', choices=difficulty)

name = inquirer.text(message="Enter your pymagotchi name")

print(f"\ngame difficulty is {level} and pet name is {name}")


class Pet():
    """Create a pymagotchi"""

    def __init__(self, name, difficulty):
        self.name = name
        self.boredom = 0
        self.dirtiness = 0
        self.hunger = 0
        self.tiredness = 0

        self.food_stock = 1
        self.game_difficulty = self.game_level(difficulty)
        self.is_alive = True
        self.round = 0

    def eat(self):
        """Deduct 1 from foodStock to lower hunger"""
        if self.food_stock > 0:
            self.food_stock -= 1
            dish = random.randint(2,4)
            self.hunger -= dish
            print(f"\n{name} ate something from the fridge worth {dish} hunger points!")
        else:
            print(f"\nFridge is empty. Go and find some food already.")

    def play(self):
        """reduce boredom value by a random int."""
        game_value = random.randint(1,4)
        if self.boredom < game_value:
            self.boredom = 0
        else:
            self.boredom -= game_value
        print(f"\n{name} had fun playing with you! ({game_value})")

    def sleep(self):
        """Set tiredness to 0"""
        self.tiredness = 0
        print(f"{name} hit the bunk! Good night, sleep tight!")

    def food_hunting(self):
        """Collect random number of food"""
        food_found = random.randint(1, 3)
        self.food_stock += food_found
        print(f"\n{name} found {food_found} food. That will keep him going for awhile")


    def bath(self):
        """reduce dirtiness"""
        bath_value = random.randint(1, 4)
        if self.dirtiness < bath_value:
            self.dirtiness = 0
        else:
            self.dirtiness -= bath_value
        print(f"\n{name} finally took a bath! It was worth {bath_value} points!")

    def time_passed(self):
        """Increase value of every attribute at the end of each round"""
        # pet_attributes = ['boredom', 'hunger', 'dirtiness','tiredness']
        pet_attributes = [self.tiredness, self.hunger, self.boredom, self.dirtiness]
        for attr in pet_attributes:
            attr += random.randint(1, self.game_difficulty)

    def show_current_status(self):
        """Shows current attributes values for a pymagotchi"""
        print(f"-----------------------------------")
        print(f"\nRound: {self.round}  {self.name} current status :")
        print(f"\nTiredness value : {self.tiredness} (0-20)")
        print(f"\nHunger value : {self.hunger} (0-20)")
        print(f"\nBoredom value : {self.boredom} (0-20)")
        print(f"\nDirtiness value : {self.dirtiness} (0-20)")
        print(f"\nFridge has food units: {self.food_stock} (0-infinity!)")
        print(f"-----------------------------------")

    def pet_activity_choice(self):
        """Show menu options for player to choose current activity for pymagotchi"""
        activities = ['play', 'eat', 'bath', 'sleep', 'food hunting']
        choice = inquirer.list_input(f"What should {self.name} do now?", choices=activities)
        if choice == 'play':
            self.play()
        elif choice == 'eat':
            self.eat()
        elif choice == 'bath':
            self.bath()
        elif choice == 'sleep':
            self.sleep()
        elif choice == 'food hunting':
            self.food_hunting()
        else:
            print('\nHow did you do that?')
            print('----------------------')
            self.pet_activity_choice()


    def game_level(self, level):
        if level == 'easy':
            return 2
        elif level == 'medium':
            return 4
        elif level == 'hard':
            return 6
        else:
            # Don't mess with me.
            return 9999


pymagotchi = Pet(name, level)

while pymagotchi.is_alive:
    pymagotchi.pet_activity_choice()
    pymagotchi.time_passed()
    pymagotchi.show_current_status()