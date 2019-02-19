print('Starting with the original list of favs: ')
pizzas = ['pepperoni', 'hawaiian', 'meatlovers']

friend_pizzas = pizzas[:]
print(friend_pizzas)

pizzas.append('chicago')
#print(pizzas)

friend_pizzas.append('extra cheese')
#print(friend_pizzas)

print("\nMy favourite Pizzas are: ")
for value in pizzas:
	print(value.title())

print("\nMy friend's favourite Pizzas are: ")
for value in friend_pizzas:
	print(value.title())