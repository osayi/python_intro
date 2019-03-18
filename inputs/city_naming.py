def city_country(city_name,country_name):
	#city_name = input("What city are you in ?")
	#country_name == input("What country would you say you are in ?")
	location = city_name.title()+ ", " + country_name.title()
	return location
	

place = city_country("venice","italy")
print(place)

place = city_country("mexico city","Mexico")
print(place)

place = city_country("port harcourt","nigeria")
print(place)