#A tuple is a collection which is ordered and unchangeable.
#Tuples are very similar to Dictionary. However they have one key difference - immutability
#Once an element is inside a tuple, it cannot be reassigned.
#Tuples us paranthesis; (1,2,3)
tuple1 = (1,2,3)
mylist = [1,2,3]

print(type(tuple1))
print(type(mylist))

t = ('a','a','b')
print(t.count('a'))
print(t.count('b'))
print(t.index('a'))
print(t.index('b'))
