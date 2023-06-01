import random

class DiceController:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return random.randint(1, self.sides)

# Example usage
dice = DiceController()  # Create a dice controller object with default 6 sides

# Roll the dice and display the result
print("Rolling the dice...")
result = dice.roll_dice()
print("The dice rolled:", result)
