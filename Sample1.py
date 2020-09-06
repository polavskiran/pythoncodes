#animal = 'cat'
#vegetable = 'broccoli'
#mineral = 'gold'
#
#print('Here is an animal, a vegetable, and a mineral.')
#print(animal)
#print(vegetable)
#print(mineral)

myname = "tinker"
#print(myname[8])
#print(myname[::2])	# print step jump from starting
#print(myname[1:4]) # print setp jump from 1st position
#print(myname[::-1]) # Reverse the string
#print(myname[::-2]) # Reverse the string step size 2

import sys
#print(sys.version)

import platform
#print(platform.python_version())

#To know the datatype of variable
x = 3
#print(type(x))

y = 35.25
#print(type(y))

z = "kiran"
#print(type(z))

x,y = 19, 82
#print(x,y)

#integer data types
int_number = 7/2
#print(int_number)

#float data type
float_number = 7.0/2
#print(float_number)

#None and boolean data types
num1 = None
#print(num1 is None)

num1 = 10
#print(num1 is None)

#Type casting
float_number = 3.6467
#print(float_number)
#print(int(float_number))
#print(str(float_number))

#Data Structure:tuples
#Tuple: A tuple is a one dimentional,immutable ordered sequence of items which can be of mixed data types.
first_tuple	=	(12,'Jack',45.6,'New',(3,2),'test')
#print(first_tuple)

#Data Structure:Slicing tuples
#print(first_tuple[1:4])	# Prints data from 1st element to 3rd element i.e 'Jack',45.6,'New'
#print(first_tuple[1:-1]) # with negative indices, it can start count from right instead of left

#Data Structure:List
#List is a one dimentional mutable ordered sequence of items which can be of mixed data types.
first_list = ['Mark',101,23.6,'Test',None,11]
#print(first_list)

first_list.append('Jack')
#print(first_list)

first_list.remove('Mark')
#print(first_list)

first_list.insert(1,'Smith')
#print(first_list)

#DataStructure:View Dictionaries
#You can view the keys and values in dict,either seperately or together, using the syntax shown here.
first_dist = {'Email':'john@gmail.com','Age':'32','Phone':'6584314546'}
#print(first_dist)

#print(first_dist.keys())
#print(first_dist.values())

#print(bin(1234))
#print(bin(128))
#print(bin(512))

#Exponentials
#The function pow() takes two arguments, equivalent to x^y. With three arguments it is equivalent to (x^y)%z, but may be more efficient for long integers.

#print(pow(3,4))
#print(pow(3,4,6))	#81%6 = 3

#Round
#The function round() will round a number to a given precision in decimal digits (default 0 digits). It does not convert integers to floats.

#print(round(3,2))
#print(round(395,-2))
#print(round(3.1415926535,2))

#DataStructure:Set
#Sets are an unordered collection of unique elements. We can construct them by using the set() function
#We can create a Set using Set keyword or using curly braces {} as follows
auto_survey = set(['Audi','BMW','BMW','Ferrari','Mercides','Toyota'])
auto_survey_set = {'Audi','BMW','BMW','Ferrari','Mercides','Toyota','GM','Chervolet'}
#print(auto_survey)
#print(auto_survey_set)

#Basic operator:in
#The 'in' operator is used to generate Boolean value to indicate whether a given is present in the container or not
student_list = ['Tom','Karl','Paul','Jimmy']
#print('Tom' in student_list)
#print('Nicky' in student_list)

word = 'Manasa'
#print('t' in word)
#print('n' in word)

#Basic Operator:+
#'+' operator produces a new tuple,list of string whose value is concatenation of the arguments
marks1 = (92,88,76)
marks2 = (78,55,89,88)
marks = marks1+marks2
#print(marks)

first_name = 'Kiran'
last_name = 'Kumar'
name = first_name +' '+ last_name
#print(name)

country_list1 = ['India','France','Russia','Israel']
country_list2 = ['UK','US','China','Brazil']
country_list = country_list1 + country_list2
#print(country_list)

#Functions
#We can define function with keyword def
#The values will be returned with return keyword, if return is not mentioned then null value will be returned
#Function overloading is not possible in python unlike in Java
def add_two_numbers(num1, num2):
    return num1+num2

number1 = 19
number2 = 91
number = add_two_numbers(number1,number2)
#print(number)

def profile():
    age = 38
    name = 'Kiran'
    height=170
    return age,name,height

age,height,name = profile() #calling the function
#print(age,height,name)

num_list = range(15)
print(list(num_list))
print(list(reversed(num_list)))

#zip function used to pair data elements of list
subjects = ['maths','physics','chemistry']
sub_count = ['one','two','three']

total_subject = zip(subjects,sub_count)
print(total_subject)
print(type(total_subject))

#Control flows:if,elif,else
age = 18

if(age > 19):
	print("major")
else:
	print("minor")

marks = 76
if(marks > 90):
    print("Grade A")
elif (80<=marks<=90):
    print("Grade B")
elif (70<=marks<=80):
    print("Grade C")
else:
    print('No Grade')

#Control flow: for loop
stock_tickers=['AAPL','GOOGL','YAHOO',None,'AMZN','CSCO','FBK']
for tickers in (stock_tickers):
    if(tickers is None):
        continue
    print(tickers)

print("================================")
stock_tickers1=['AAPL','GOOGL','YAHOO',None,'AMZN','CSCO','FBK']
for tickers in (stock_tickers1):
    if(tickers is None):
        break
print(tickers)

#Control flow: while loop
temperature = 100
while temperature > 95:
    print(temperature)
    temperature =   temperature - 1

#Control flow: exception handling
#we can use try/except for exception handling
def test_float(number):
	try:
		return print(float(number))
	except ValueError:
		return print('Not a number, the input value is: ',number)

test_float(3.1456)
test_float('test float')