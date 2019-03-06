rivers = {
	'nile' : 'egypt',
	'niger' : 'nigeria',
	'congo' : 'congo',
	'benue' : 'nigeria',
	'mississipi' : 'usa'
}

for river, country in sorted(rivers.items()):
	print("The river " + river.title() + " runs through " + country.title())

print('\nThese are major rivers:')
for river in sorted(rivers.keys()):
	print(river.title())

print('\nThese countries have major rivers running through them:')
for country in set(rivers.values()):
	print(country.title())
