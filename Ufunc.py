import numpy as np

#numpy.sqrt
#Returns non-negative square root  of given number
np_sqrt = np.sqrt([2,4,8,9])
#print(np_sqrt)

#numpy.cos
#Trigonometric cosine element wise
np_cos = np.cos(np.array([0, np.pi/2, np.pi]))
#print(np_cos)
#print(np.pi)

#numpy.sin
#Trigonometric sine, element-wise
np_sine = np.sin(np.array([0, np.pi/2, np.pi]))
#print(np_sine)

#numpy.floor
#Return the floor of the input, element-wise.
np_floor = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
#print(np.floor(np_floor))

#Shape manipulation
#WE can use certain functions to manipulate array shape
#numpy.hsplit
#Split an array into multiple sub-arrays horizontally(column-wise).
arr = np.arange(15).reshape(5,3)
#print(arr)
arr_hsplit = np.hsplit(arr,3)
#print(arr_hsplit)

#Shape Manipulation - Example
#You can use certian functions to manipulate the shape of an array by doing the folowing:

#numpy.ravel
#Return a continuous flattened array.
cyclist_trials = np.array([[10,15,27,26],[12,11,12,24]])
cyclist_trials = np.ravel(cyclist_trials)
print(cyclist_trials)

#numpy.reshape
#Gives a new shape to an array without changing its data.
new_shape_cyclist_trials = cyclist_trials.reshape(4,2)
print(new_shape_cyclist_trials)

#numpy.resize
#Return a new array with the specified shape.
#If the new array is larger than the original array, then the new array is filled with repeated copies of a.
arr = np.array([[0,1],[2,3]])
arr1 = np.resize(arr,(2,3))
print(arr1)

#Linear algebra - Transpose
#transpose() function can help you to interface rows as columns and vice-versa
cyclist_trials = np.array([[10,15,27,26],[12,11,12,24]])
print(cyclist_trials)
print(cyclist_trials.transpose())

#numpy.linalg.inv
#compute the multiplicative inverse of a matrix.
inverse_array = np.array([[30,40],[45,56]])
print(np.linalg.inv(inverse_array))

#numpy.trace
#Returns the sum along the diagonals of the array
arr = np.array([[30,40],[45,56]])
print(np.trace(arr))

arr1 = np.arange(24).reshape((2,2,2,3))
print(arr1)