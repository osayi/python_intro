#setting up a python script to read a text file


with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)