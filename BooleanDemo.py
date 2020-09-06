#Indexing with boolean arrays

import numpy as np

test_scores = np.array([[83,71,55,66],[45,63,96,76]])
passing_score = test_scores>60
print(passing_score)
print(test_scores[passing_score])

#Copy and Views
#View/Shallow copy
#A view, also referred to as a Shallow copy, creates a new array object
Boroughs_in_NYC = np.array(['Manhatta','Bronx','Brooklyn','Staten Island','Queens land'])
print(Boroughs_in_NYC)

View_of_Boroughs_in_NYC = Boroughs_in_NYC.view()
print(len(View_of_Boroughs_in_NYC))

#Change 5th element in View_of_Boroughs_in_NYC
View_of_Boroughs_in_NYC[4] = 'Central Park'
print('Upated array is:')
print(View_of_Boroughs_in_NYC)
#New Array Boroughs_in_NYC is
print('New Array Boroughs_in_NYC is:')
print(Boroughs_in_NYC)

#Copy. copy is also called as 'Deep copy' because it entirely copies the original dataset.
#Any change in the copy will not efffect the original dataset.
copy_of_Boroughs_in_NYC = Boroughs_in_NYC.copy()
print(copy_of_Boroughs_in_NYC is Boroughs_in_NYC)
print(copy_of_Boroughs_in_NYC.base is Boroughs_in_NYC)

#change copy_of_Boroughs_in_NYC[4]
copy_of_Boroughs_in_NYC[4] = 'Queens land'
print('Original dataset after change is')
print(Boroughs_in_NYC)
print('Copy dataset after change is:')
print(copy_of_Boroughs_in_NYC)