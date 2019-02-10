#experimenting with car lists
cars = ['honda', 'subaru', 'chevrolet', 'mercedes benz']

print(cars)

cars.append('jeep')  #adding a new car to the end of the list
print(cars)

cars.insert(1, 'mazda') #inserting a new car in the middle of the list
print(cars)

del cars[2]  # deleting an item from the list
print(cars)

popped_car = cars.pop()  # popping the last item out of the list
print ('\nThe last car I looked into buying was a ' + popped_car)
print(cars)

popped_car = cars.pop(1)  #pooing any item on the list
print('\nThe second car I looked into was the ' + popped_car)


cars.append('volkswagen')
cars.append('audi')
print(cars)

too_expensive = 'mercedes benz'
cars.remove(too_expensive)
print ('The ' + too_expensive + ' was too expensive man!')
