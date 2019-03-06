prompt = "Welcome to Pizza-O's! Type in any topping: "
prompt += "\nType 'quit' if you're done adding toppings."

topping = ""
toppings = []

while topping != 'quit':
	topping = input(prompt)
	toppings.append(topping)

	if topping != 'quit':
		print("We'll throw " + topping.title() + " on your pizza! Want any more?")
		
	else:
		print("Thanks! We'll get your order ready!")

print('These are your toppings!')
for top in toppings:
	if top != 'quit':
		print(top.title())
