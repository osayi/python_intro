#checking usernames on a website

current_users = ['esosa', 'eromose', 'ayobami','onos', 'chikezie']

new_users = ['matt', 'Esosa', 'harnor', 'suyi', 'sadiq']
	
for current_user in current_users:
	for new_user in new_users:
		if current_user.lower() == new_user.lower():
			print("Sorry " + current_user + " is already taken.")
			break
	else:
		print("You're in luck! "+current_user+" is available.")