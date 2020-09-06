#def odd_or_even(number):
#    """Determine if a number is Odd or Even."""
#    if number%2 == 0:
#        return 'Even'
#    else:
#        return 'Odd'
#
#testnum = odd_or_even(6)
#print(testnum)

def getName():
    name = input('What is your name? ')
    return name

def setName(name):
    print('Your name is {}.'.format(name))

def get_and_set_name():
    """Get and Display Name"""
    name = getName()
    setName(name)

get_and_set_name()