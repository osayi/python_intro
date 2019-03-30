# Creating an ice cream stand that inherits from the 
# restaurant class

class Restaurant():
	'''A restaurant with a name and cuisine.'''
	def __init__(self,name,cuisine):
		'''Initializing name and cusine'''
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0

	def describe_restaurant(self):
		'''Describing the name and cuisine of the restaurant'''
		print("Welcome to " + self.name.title() + ", we serve " + self.cuisine.title() + " cuisine.")

	def open_restaurant(self):
		print("We're now open!")

	def served(self):
		print("The number of customers served is " + str(self.number_served))

	def set_number_served(self, now_served):
		self.number_served = now_served

	def increment_number_served(self):
		self.number_served += 25

class IceCreamStand(Restaurant):
	''' An ice cream stand inheriting from restaurant'''
	def __init__(self, name, cusine):
		''' Initialize from the restaurant class'''
		super().__init__(name, cusine)
		self.flavors = ['vanilla','chocolate','coffee',
				 		'strawberry','mango','cookie dough','cookies and cream']

	def flavour_list(self):
		print("\nChoose from the following ice cream flavours:")
		for flavour in self.flavors:
			print(flavour.title())


my_icecream = IceCreamStand('sayi','desert')
my_icecream.describe_restaurant()
my_icecream.flavour_list()


