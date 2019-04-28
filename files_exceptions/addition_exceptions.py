

print("Select two numbers and I will give you their sum.")
print("Press 'q' at any prompt to quit.")

while True:
	first_number = input("Pick your first number:\n")
	if first_number == 'q':
		print(" Thanks for your time, Good luck!")
		break

	second_number = input("Pick your second number:\n")
	if second_number == 'q':
		print(" Thanks for your time, Good luck!")
		break

	try:
		sum = int(first_number) + int(second_number)
	except ValueError:
		print("Please make sure you're using integers and not spelling out the number. ")
	else:
		print("The sum of those 2 numbers is, " + str(sum) + ".")
		
