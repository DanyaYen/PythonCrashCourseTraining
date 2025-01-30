import random
class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_dice(self):
        return random.randint(1, self.sides)
        
dice = Dice()
for i in range(10):
    res = dice.roll_dice()
    print (f'{i+1}: {res}')

twenty_sided_die = Dice(20)
print("\nRolling a 20-sided die 10 times:")
for roll in range(10):
    result = twenty_sided_die.roll_dice()
    print(f"Roll {roll + 1}: {result}")