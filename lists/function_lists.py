#all the functions - length, sorted, 
#all the methods - sort, remove, pop, append, title

seasons = ['autumn', 'winter', 'spring', 'summer', 'dry', 'rainy']

#length of array
print(len(seasons))

#temporary sort only displays original data sorted
print(sorted(seasons))

print (seasons)

#pop method allows me use the name item I'm getting rid off

#cold = seasons.pop(1)

print('\nI am really tired of the ' + seasons.pop(1) + '!')

print(seasons)

#append method allows add a new item to the array or list

seasons.append('winter')

print('\nAlthough I could not wait for ' + seasons[-1] + ' so I can really start dressing')

#titling each of the items in an array

print(seasons[3].title())
print(seasons)
#removing an item permanently

seasons.remove('dry')
print(seasons)

#permanent chronological ordering 

seasons.sort()
print(seasons)
