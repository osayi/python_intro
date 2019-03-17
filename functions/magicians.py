magic_stars = ['houdini', 'cris angel', 'david blaine']

def show_magicians(magicians):
	''' We will be showing the names of each magician in 
		any given list of magicians
	'''
	for magician in magicians:
		print("Please welcome the Great... " + magician.title() + "!!")

#show_magicians(magic_stars)

great_magicians = []

def make_great(magicians, greats):
	''' Here we will create a new list where all the magic stars 
		will have "great" next to their name
	'''
	#for magician in magicians - why does this skip a parameter
	while magicians:
		curent_magician = magicians.pop()
		curent_magician = "the Great " + curent_magician.title()
		great_magicians.append(curent_magician)
	print(great_magicians)	

make_great(magic_stars[:], great_magicians)
show_magicians(magic_stars)
print(magic_stars)
