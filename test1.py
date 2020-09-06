mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c','d','e','f']
mylist3 = [100,200,300,400,500]

zip(mylist1,mylist2,mylist3)

for item in zip(mylist1,mylist2,mylist3):
    print(item)