import json

#username = input("What is your username")
fav_number = input("Hi There! What's your favourite number? ")

filename = 'fav_number.json'

with open(filename, 'w') as f_obj:
	json.dump(fav_number, f_obj)
	print("Your favourite number is now stored")

with open(filename) as f_obj:
	fav_number = json.load(f_obj)
	print("Welcome back, I know your favourite number is " + fav_number + "!")

	