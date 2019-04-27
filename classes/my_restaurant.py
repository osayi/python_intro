''' Simple restaurant instance that pulls from the parent class'''
from restaurant_class import Restaurant

my_restaurant = Restaurant('scaddabush','italian')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


restaurant = Restaurant('la grota', 'italian')
restaurant.describe_restaurant()
restaurant.served()
restaurant.number_served = 170
restaurant.served()
restaurant.set_number_served(450)
restaurant.served()
restaurant.increment_number_served()
restaurant.served()