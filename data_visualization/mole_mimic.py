from random import choice

class RandomWalker():
	'''A class to descrbe how atrributes up and 
	down will move ramdomly'''

	def __init__(self, tot_points=7000):
		''' initializing total number of points to be walked'''
		self.tot_points = tot_points

		''' setting points to begin at origin'''
		self.vert_values = [0]
		self.hor_values = [0]

	def walk_path(self):
		''' calculate all the steps or points in walk'''
		
		'''this sets the vertical values at a max of 7000'''
		while len(self.vert_values) < self.tot_points:
			'''deciding where and how far it will go vertically'''
			vert_direction = choice([1,-1])
			vert_distance = choice([0,1,2,3,4])
			vert_steps = vert_direction * vert_distance

			'''deciding where and how far it will go horizontally'''
			hor_direction = choice([1,-1])
			hor_distance = choice([0,1,2,3,4])
			hor_steps = hor_direction * hor_distance

			if hor_steps == 0 or vert_steps ==0:
				continue


			'''calculate the next steps'''

			next_vert = self.vert_values[-1] + vert_steps
			next_hor = self.hor_values[-1] + hor_values


			self.vert_values.append(next_vert)
			self.hor_values.append(next_hor)

			


