#describing the country a city is based in

def describe_city(city, country="Canada"):
	""" Printing out the city and the country """
	print("The city " + city.title() + " is in " + country.title())


describe_city('winnipeg')
describe_city('montreal')
describe_city('ikeja','nigeria')