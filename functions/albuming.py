def make_album(artist_name, album_title , track_no ='', album_year =''):
	albums = {'artist': artist_name, 'title': album_title}

	if track_no:
		albums['tracks'] = track_no

	if album_year:
		albums['year'] = album_year

	return albums


album = make_album('eminem', 'eminem show', '17', '2001')
print(album)

album = make_album('kaytranada', '99.9%', '13')
print(album)
album = make_album('50 cent','get rich or die tryin')
print(album)



listening = True
while listening:
	#establishing a prompt to let the user know what we may be asking 
	prompt = input("Got a sec for a question on music? yes/no ")

	#check if user is interested in hearing question
	if prompt == 'no':
		listening = False
	else:
		#requesting info from the user on their current music taste
		artist_name = input("What artist have you been listening to lately?")
		album_title = input("What album is the track you're listening to ?")

		album = make_album(artist_name,album_title)
		print(album)
		
		
	
	

	


	
