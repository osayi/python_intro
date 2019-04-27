
from random import randint

class Die():
	''' new program for dice using random class'''
	def __init__(self, sides='6'):
		self.sides = sides

	def roll_die(self):
		self.sides = randint(1,6)
		print(self.sides)

	def roll_die_ten(self):
		self.sides = randint(1,10)
		print(self.sides)

	def roll_die_20(self):
		self.sides = randint(1,20)
		print(self.sides)



my_dice = Die()

my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
print('\n')
my_dice.roll_die_ten()
my_dice.roll_die_ten()
my_dice.roll_die_ten()
print('\n')
my_dice.roll_die_20()
my_dice.roll_die_20()
my_dice.roll_die_20()

