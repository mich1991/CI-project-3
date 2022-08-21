# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import inquirer

difficulty = ['easy', 'medium', 'hard']
level = inquirer.list_input('Choose difficulty level', choices=difficulty)

name = inquirer.text(message="Enter your pymagotchi name")

print(f"game difficulty is {level} and pet name is {name}")
