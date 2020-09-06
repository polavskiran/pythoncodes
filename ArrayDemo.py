#ndarray.ndim
#Numpy's array class is "ndarray", also referred as "numpy.ndarray".
#The attributes of ndarray are
#ndarray.ndim, ndarray.shape,ndarray.size,ndarray.dtype

import numpy as np

np_city = np.array(['Delhi','Mumbai','Chennai','Kolkata','Hyderabad','Bengaluru','Vizag','Gurgaon','Noida'])
#print(np_city.ndim)
some_cities = np_city[2:5]
print(some_cities)

first_two = np_city[0:2]
print(first_two)

firsttwo = np_city[:2]
print('First two cities: {} '.format(firsttwo))

#try/except example
try:
    city_index = np_city['Guntur']
except:
    city_index  =   'No Such city found'
print(city_index)

for city in np_city:
    print(city.lower())

#help('FORMATTING')

np_city_with_state = np.array([['Delhi','Mumbai','Chennai','Kolkata'],['Delhi','MH','TN','WB']])
#print(np_city_with_state.ndim)

#Share of the Objects
#print(np_city.shape)
#print(np_city_with_state.shape)

#ndarray.size
#It gives the total number of elements in the array.
#It is equal to the product of the elements of the shape tuple
#print(np_city.size)
#print(np_city_with_state.size)

#ndarray.dtype
#It's an object that describes the type of the elements in array.
#It can be created or specified using python
#print(np_city.dtype)
#print(np_city_with_state.dtype)

#Basic operations on Array elements
#print(np.add(45,20))
#print(np.subtract(45,20))

#ndarray multiplication
#create ndarray which contains number of hours worked each for 5 days
#daily wage for each day is USD 15
np_daily_wage = np.array([7,9,13,8,19]) * 15

#print hourly wage for each day
print(np_daily_wage)

#total earnings after 5 days
sum_daily_wage = sum(np_daily_wage)
print(sum_daily_wage)

#crate an ndarray for weekly hrs, 5 consecutive weeks hrs data
np_weekly_hrs = np.array([23,41,55,47,39])

#get weekly hrs more than 40
#print(np_weekly_hrs[np_weekly_hrs>40])

#Logical AND operation
#print(np.logical_and(np_weekly_hrs>20,np_weekly_hrs<50))

#Logical NOT  operation
#print(np.logical_not(np_weekly_hrs>35))

#Accessing array elements : Indexing
cyclist_trials = np.array([[10,15,27,26],[12,11,12,24]])

first_trial =   cyclist_trials[0]
second_trial = cyclist_trials[1]
print(first_trial)
print(second_trial)

#First cyclist: first trial data
first_cyclist_firstTrial = cyclist_trials[0][0]
print(first_cyclist_firstTrial)

first_cyclist_all_trials = cyclist_trials[:,0]
print(first_cyclist_all_trials)

#Accessing array elements : Iteration
print("Using for loop to print array: ")
for iterate_cyclist_data in cyclist_trials:
    print(iterate_cyclist_data)

names = np.array(['Kiran','SWathi','Manasa','Laalasa'])
years = np.array([1982,1986,2013,2017])

for index in range(len(names)):
	print('Name:', names[index],'Year of birth:',years[index])

animals = ['tiger','lion','bear','fox'];
print(animals.index('bear'))
