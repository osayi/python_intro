#code will show user and their ideal vaccation destination

destinations = {}

#set a flag that show the destinations poll is active

polling_active = True

while polling_active:
	#Prompt for name and destinaton
	name = input("What is your name? \n")
	destination = input("What is your dream vacation destination? \n")

	#store name and destination in dictionary
	destinations[name] = destination

	prompt = input("Thanks for your time, is another person available to take the pole? (yes/no) ")

	if prompt == 'no':
		print("Thanks for taking the Poll!")
		polling_active = False

print("\n---- Poll Results ----\n")
for name, destination in destinations.items():
	print(name.title() + " selected " + destination.title() + " as their dream location!")
