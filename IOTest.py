myfile = open('myfile.txt')
print(myfile)
print(myfile.read()) 
#Once file read complets cursor will be at end of file
# hence, print(myfile.read()) will print nothing
# so, we use below condition to read file from beginning
myfile.seek(0)
print(myfile.read()) 
