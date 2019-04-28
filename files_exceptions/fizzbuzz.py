
#defining number as num
'''
num = 1
while num < 101:
	
	output = num
	
	if num % 15 == 0:
		output = "fizzzbuzz"
		print(output)
		num += 1
		

	elif num % 5 == 0:
		output = "buzzz"
		print(output)
		num += 1
		

	elif num % 3 == 0:
		output = "fizz"
		print(output)
		num += 1
		
	elif num % 1 == 0:
		output = num
		print(output)
		num += 1
'''		


#second attempt
#defining value as number

for value in range(1,101):
	output = value
	if value % 15 == 0:
		output = "fizzbuzz"
	elif value % 3 == 0:
		output = "fizz"
	elif value % 5 == 0:
		output = "buzz"
	else:
		output = value
	print(output)

