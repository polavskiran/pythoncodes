#This file tells about dictionary object
contacts = {
        'Kiran':{
            'Phone' : '9873969385',
            'Email' : 'pvs.kiranmca@gmail.com'
        },
        'Swathi':{
            'Phone' : '8447134211',
            'Email' : 'test1@gmail.com'
        }
}

#Looping with 2 variables
for Person,Details in contacts.items():
    print('Name is {0} and details are {1}'.format(Person,Details))