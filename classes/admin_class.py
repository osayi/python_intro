from users_class import User


class Privileges():
	'''New prvilege class to be use for admin
		and possibly more users'''
	def __init__(self, privileges=['can add post','can delete post','can ban user']):
		self.privileges = privileges

	def show_privileges(self):
		print("The administator: " + str(self.privileges))
		'''for privilege in self.privileges:
			print(privilege)'''

class Admin(User):
	'''Creating an admin class with special ptvileges'''

	def __init__(self, first_name, last_name):
		'''Initializing admin with privileges'''
		super().__init__(first_name, last_name)
		self.priv = Privileges()
		#self.privileges = ['can add post','can delete post','can ban user']






