#program to display movie tickets by age group

age = input("Welcome to Movie-O's, type in your age for movie ticket prices: ")
age = int(age)

active = True

while active:
	if age < 3:
		print("Hey you little toddler your ticket is free!")
		continue

	elif age <= 12:
		print("Hey young one, will you have $10 for the ride? ")
		break

	elif age > 12:
		print("Hey there, you'll be paying $15 for the ride.")
		break

