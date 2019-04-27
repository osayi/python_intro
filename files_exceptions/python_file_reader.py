# this program reads the 'learning_python' file

with open('learning_python.txt') as file_object:
	contents = file_object.read()
	print(contents)

print('\n')
with open('learning_python.txt') as file_object:
	for content in file_object:
		content.replace('python','C++')
		print(content.strip())

print('\n')

#contents = []
with open('learning_python.txt') as file_object:
	contents = file_object.readlines()


for content in contents:
	print(content.rstrip())

message = "fuck you pay me!"
message.replace('pay', 'kiss')
print(message)