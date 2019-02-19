# Countries to visit
places = ['Cuba','spain','morocco','japan','fiji','australia', 'South Africa']


if places[1] == 'spain':
	print("Are you visiting " + places[1]+ " ? I might stop by there! ")

if places[0].lower() == 'cuba':
#if places[0] == 'cuba':
 	print("OH, true say, you're headed to " + places[0] + "? Damn, don't think I can make it. ")

print(len(places))

if len(places) >= len(places[1:4]):
	print("That's over half of your list")

place = 'dubai'
if place not in places:
	print("Oh shoot! I didn't even think of "+place.title()+"!")