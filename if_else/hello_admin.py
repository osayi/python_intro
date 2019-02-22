#printing username greetings upon sign in

#usernames = ['admin', 'esosa', 'eromose', 'ayobami','onos', 'chikezie']
usernames = []

if usernames:
	for username in usernames:
		if username == 'admin':
			print("Hello " + username.title() + ", welcome back! Would you like a status report?" )
		else:
			print("Hi " + username.title() + ", thanks for logging back in!")
else:
	print("You're not a user, sign up now!")