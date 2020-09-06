import numpy as np
from scipy import linalg

matrix = np.array([[10,6,8],[2,7,5],[4,7,6]])
print(matrix)

invmatrix = linalg.inv(matrix)
print(invmatrix)

determinent = linalg.det(matrix)
print(determinent)

#Solve linear systems
#Solve below
#2x+3y+z = 21, -x+5y+4z=9, 3x+2y+9z = 6
numArray = np.array([[2,3,1],[-1,5,4],[3,2,9]])
numArrValue = np.array([21,9,6])
xyzValues = linalg.solve(numArray,numArrValue)
print('X,Y,Z Values are {}'.format(xyzValues))