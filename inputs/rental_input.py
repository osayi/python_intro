# list of rental cars that we have

rentals = ['subaru','audi','honda','volkswagen','toyota']

selection = input("Please type in the model of car you would like to rent: ")



for rental in rentals:
	if selection.lower() == rental:
		print("You're in luck! We have a " + selection.title() + " in the lot!")
		break
else:
	print("Unfortunately we don't have this brand in stock, would you like to pick another? ")
	#need to figure out a way to jump back into the start of the loop
	selection = input("Please type another model of car you would like to rent: ")
