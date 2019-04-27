#dictionary containing my perdonal details

'''use OrderedDict class to ernsure, values are recorded chronologically'''

from collections import OrderedDict

person = OrderedDict()
fav_numbers = OrderedDict()
glossary = OrderedDict()

person = {
	'first name' :'osayi',
	'last_name': 'okuns',
	'age' :'28',
	'city' :'toronto',
}

print(person)

fav_numbers = {
	'bugs bunny' : 7,
	'daffy duck' : 3,
	'road runner' : 10,
	'tweety' : 5,
}

print(fav_numbers)

glossary = {
	'elif' : 'else if, is used if you want to add more conditions beyond if or else.',
	'lists' : 'lists (or arrays) are used to record a number of variables in one group.',
	'loop' : 'loops, allow for use to go though a list or dictionary of values.',
	'strings' : 'strings are how we define words and sometimes numbers, it needs to be printed.',
	'comments' : 'comments, are a way of describing and providing context to your code particularly as things get more complicated.',
}

for name, meaning in (glossary.items()):
	print(name.title() + ":\n     " + meaning)

#for meaning in glossary.values():
#	print( "Guess the names of this definition:\n     " + meaning)
