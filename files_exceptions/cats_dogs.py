
filenames = ['cats.txt','dogs.txt','trash.txt']

for filename in filenames:
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		#message = "Sorry the fie you're looking for isn't in this directory"
		#print(message)
		pass
	else:
		print("List of pets stored in: " + filename)
		print(contents + '\n')
