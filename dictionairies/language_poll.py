languages = {
	'tristan' : 'javascript',
	'charla' : 'java',
	'terrence' : 'ruby',
	'andrew' : 'c++',
	'taylor' : 'python',
	'dreezy' : 'sql',

}

new_applicants = ['sayi','kim','charla','andrew','matt']

for new_applicant in sorted(new_applicants):
	for name,language in languages.items():
		if new_applicant == name:
			print("Hi "+new_applicant.title()+", I see you like to code in "+language)
			break
	else: print(new_applicant.title() +" please take our poll on your favourite coding language.")

