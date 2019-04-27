#We're creating a restaurant class with a name and cuisine type

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
		print("The number of customers served at " + self.name.title() + " is " + str(self.number_served))	

	def set_number_served(self, now_served):
		self.number_served = now_served

	def increment_number_served(self):
		self.number_served += 25


