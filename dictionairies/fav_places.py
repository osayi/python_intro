favourite_places = {
	'osayi': ['fiji', 'iceland','australia'],
	'ivie' : ['paris', 'santorini', 'saint tropez'],
	
}

for name, places in sorted(favourite_places.items()):
	print('Hi I am ' + name.title() + ' and I would love to visit:')
	for place in places:
		print('\t' +  place.title())
	print('\n')

