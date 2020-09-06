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