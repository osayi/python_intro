
def word_counter(filename, word):
	'''Counting the approximate number of 
		a selected word in a file'''
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		#message = "Sorry the fie you're looking for isn't in this directory"
		#print(message)
		pass
	else:
		print("We counted the number of times '" + word + "' was stored in: " + filename)
		word_count = contents.lower().count(word)
		print("We found '"+ word.title() + "' " + str(word_count) +' times \n')


word_counter('sherlock.txt',"baker")
word_counter('jekyll_hyde.txt','jekyll')



