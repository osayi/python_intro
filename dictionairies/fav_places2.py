fav_places = {
	'sayio':{
		'name' : 'osayi',
		'places' : ['fiji', 'iceland','australia'],
		},
	'iviea':{
		'name' : 'ivie',
		'places' : ['paris', 'santorini', 'saint tropez'],
		}
}


for username, userinfo in fav_places.items():
	print(userinfo['name'].title() + ' would like to visit:')
	for place in userinfo['places']:
		print(place.title())
	print('\n')
