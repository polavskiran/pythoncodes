class Addition:
    first = 0
    second = 0
    addition = 0
    subtraction = 0

    def __init__(self, f,s):
        self.first = f
        self.second = s

    def Display(self):
        print("First = " + str(self.first))
        print("Second = " + str(self.second))
        print("Addition of two numbers is = "+ str(self.addition))
        print("Subtraction of two numbers is = "+ str(self.subtraction))

    def calculate(self):
        self.addition = self.first + self.second
        self.subtraction = self.first - self.second


#creating the object of the class
obj = Addition(786,786)

#perform calculation
obj.calculate()

#Display values
obj.Display()