# decorator - function that modifies the behavior of another function without changing its actual source code 

# syntax - @decorator_name 

# example - 
def my_decorator(func) : 
    def wrapper() : 
        print("Something before") 
        func() 
        print("Something after") 
    return wrapper 

@my_decorator 
def say_hello() :   # this is actual function - goes as an argument to our decorater funciton 
    print("Hello") 

say_hello() 


