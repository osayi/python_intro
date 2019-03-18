
def make_car(manufacturer, model, **car_info):
	car = {}
	car['car_manufacturer'] = manufacturer
	car['car_model'] = model

	for key, info in car_info.items():
		car[key] = info

	return car

new_car = make_car('mercedes', 's-class', car_type='sedan', car_colour='navy blue')

print(new_car)