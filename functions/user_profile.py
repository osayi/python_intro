def build_profile(first,last,**user_info):
	'''This dictionary will collect any relevant info of the user'''
	profile = {}
	profile['first name'] = first
	profile['last name'] = last

	for key,info in user_info.items():
		profile[key] = info

	return profile

user_profile = build_profile('david','beckham',team='L.A Galaxy',age=42)

print(user_profile) 