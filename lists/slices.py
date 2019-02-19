places = ['cuba','spain','morocco','japan','fiji','australia', 'South Africa']

print("The first three items in the list are: ")
for value in places[0:3]:
	print(value.title())

print("\nThe items from the middle of the list are: ")
for value in places[3:6]:
	print(value.title())

print("\nThe last three items inn the list are: ")
for value in places[-3:]:
	print(value)