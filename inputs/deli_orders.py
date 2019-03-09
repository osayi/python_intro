# a list of sandwich orders

sandwich_orders = ["pastrami sandwich", "egg sandwich", "ham sandwich", "pastrami sandwich", "chicken sandwich", "tuna sandwich", "pastrami sandwich"]
finished_sandwiches = []

#while lopp through sandwich order list
#later remove repeate items

print("Make your order, please note we've run out of Pastrami.")
while sandwich_orders:
	current_order = sandwich_orders.pop()
	if current_order != "pastrami sandwich":
		print("We're making your " + current_order.title())
		finished_sandwiches.append(current_order)


print("\nWe made the following sandwiches!\n")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())