
def make_sandwich(*condiments):
	'''Placing items that would be placed in the sandwich'''
	print("Based on your order your, your sandwich will contain:")
	for condiment in condiments:
		print('-' + condiment)