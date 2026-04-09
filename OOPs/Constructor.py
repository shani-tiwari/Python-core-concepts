
# constructor is a special method that is called automatically when we call a class
# constructor is used to initialize the object

class ClassName : 
    # constructor to initialize attributes
    def __init__(self,name,model,year) :
        self.name = name    # instance attribute
        self.model = model
        self.year = year
    # method to show/display data
    def display(self):    # instance method
        print("Name : ",self.name)
        print("Model : ",self.model)
        print("Year : ",self.year)

    def normal() :     # normal method
        print()

# creating objects
car1 = ClassName("Toyota", "Camry", 2022)
car2 = ClassName("Honda", "Civic", 2023)
car3 = ClassName("Tata", "Nexon", 2024)

# calling functions
car1.display()
car2.display()
car3.display()  


## types of attributes 

    # 1. instance attributes
class instance() : 
    def fun(self, a) : 
        self.a = a # instance attribute

'''
    2. class attributes --- normal variable
    3. static attributes
    4. local attributes
'''

# types of methods
    # 1. instance methods
def display(self):          # instance method 'self' used , self target to object location
    print("Name : ",self.name)

    # 2. class methods
@classmethod
def display(cls):          # cls target to class location
    print("Name : ",cls.name)

    # 3. static methods
@staticmethod
def display():          # target to object location
    print(" hi ")

