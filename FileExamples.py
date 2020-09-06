with open('myfile.txt') as my_new_file:
	contents = my_new_file.read()

#print(contents)

with open('myfile.txt', mode='r') as new_file:
	filecontents = new_file.read()

print(filecontents)