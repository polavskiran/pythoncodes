##print('{0:8} | {1:<8}'.format('Fruit','Quantity'))
##print('{0:8} | {1:<8}'.format('Apple','3'))
##print('{0:8} | {1:<8}'.format('Oranges','10'))

#print('I {} python.'.format('love'))
#print('{} {} {}.'.format('I','love','python'))

def say_Hi(name):
    print('Hi {}!'.format(name))

#say_Hi('Kiran')

def sayHi(name = 'there'):
    print('Hi {}!'.format(name))

sayHi()
sayHi('Kiran')

def sayHi(firstname,lastname):
    print('Hi {} {}!'.format(lastname,firstname))

sayHi(firstname='Kiran',lastname='Kumar')
sayHi(lastname='Kumar',firstname='Kiran')