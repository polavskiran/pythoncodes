import numpy as np

distance = [10,15,17,26]
time = [.30,.47,.55,1.20]

np_distance = np.array(distance)
#print(np_distance)

np_time = np.array(time)
#print(np_time)

speed = np_distance/np_time
#print(speed)

array_with_zerors = np.zeros((3,2));
#print(array_with_zerors)

#array with random numbers, please use it with caution
array_with_empty = np.empty((2,3))
#print(array_with_empty)

#array with arange method
np_arange = np.arange(15)
#print(np_arange)

#Reshare method to change/create array
#print(np_arange.reshape(5,3))

np_linspace = np.linspace(4,13,7)
print(np_linspace)

#1-D, 2-D and 3-D arrays using arange,reshape methods
one_Darray = np.arange(12)
#print(one_Darray)

two_Darray = np.arange(12)
#print(two_Darray.reshape(3,4))

three_Darray = np.arange(27).reshape(3,3,3)
#print(three_Darray)