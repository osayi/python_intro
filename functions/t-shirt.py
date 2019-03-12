#creating a make t-shirts funcion

def make_shirt(size='Large', statement='I love Python.'):
	"""Display info on t-shirt"""
	print("You ordered a " + size.title() + " T-shirt that says '" + statement +"' on it. " )
	print("Hope it fits well!")

#make_shirt('X-Large', 'Super dope!')
#make_shirt(size="Large", statement="Packing Heat")

make_shirt()
make_shirt('Medium')
make_shirt('Small', 'Fuck that!')