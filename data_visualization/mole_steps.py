from random import choice

class RandomWalk():
	"""A class to generate random walks."""
	def __init__(self,num_points=5000):
		"""Initialize attributes"""
		self.num_points = num_points

		"""Setting all walks to start from(0,0)"""
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""Calculate all the points in the walk."""

		#Keep taking steps until you hit the max of 5000
		while len(self.x_values) < self.num_points:

			def get_step(self):
				
				self.direction = choice([1,-1])
				self.distance = choice([0,1,2,3])
				self.step = self.direction * self.distance
			
				#Disregarding moves that go nowhere
				if self.step == 0:
					return

			x_step = get_step()
			y_step = get_step()

			#Calculate the next steps
			next_x = self.x_values[-1] + x_step 
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)
	