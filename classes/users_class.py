# creating a user for a login platform
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

'''
new_user = User('osayi', 'okuns')
new_user.describe_user()
new_user.greet_user()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
logins = new_user.login_attempts
print(logins)
new_user.reset_login_attempts()
logins = new_user.login_attempts
print(logins)


next_user = User('ivy', 'agbons')
next_user.describe_user()
next_user.greet_user()
'''
