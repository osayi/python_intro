filename = 'guest_booker.txt'

prompt = 'Can you please tell me your name \n(or type "no" otherwise): '

with open(filename, 'w') as file_object:
	while prompt != 'no':
		message = input(prompt)
		file_object.write(message + '\n')
		if message == 'no':
			print('Thanks for stopping by')
			break






