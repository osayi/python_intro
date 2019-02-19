
country = "zimbabwe"

if country != "nigeria":
	print ("You will need to visit Nigeria, Africas Giant!" )
	print(country.title() + ' is cool tho')


country = "usa"
if country == 'usa':
	print("\nOhh! You are from the " + country.upper() + "? Lucky you, you get to call Trump your President -__-")



places = ['cuba','spain','morocco','japan','fiji','australia', 'South Africa']

place = 'cuba'

if place in places:
	print("\nI'm planning to visit " + place.title() + " in the near future!")

place = 'germany'

if place not in places:
	print(place.title() + " might be fun, but it's not on my shortlist for vacation.")