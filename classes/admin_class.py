class User():
	''' Creating a model for each user'''
	
	def __init__(self, first_name, last_name):
		''' Defining the user attributes'''
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		'''Identifying user based on attributes'''
		print("Hi I'm " + self.first_name.title() + " " +self.last_name.title())

	def greet_user(self):
		print("Good morning " + self.first_name.title() + " have a great day!" )

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

class Admin(User):
	'''Creating an admin class with special ptvileges'''

	def __init__(self,first_name,last_name):
		'''Initializing admin with privileges'''
		super().__init__(first_name,last_name)
		self.privileges = ['can add post','can delete post','can ban user']

	def show_privileges(self):
		print("The administator: ")
		for privilege in self.privileges:
			print(privilege)

new_admin = Admin('sayi','ao')
new_admin.show_privileges()
