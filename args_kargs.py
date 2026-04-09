

def add(*args) : # *args - means any number of arguments can be passed as a tuple 
    print(args) 
    print(type(args)) # tuple   

add(1, 2, 3, 4, 5) 



def add(**kwargs) : # **kwargs - means any number of keyword arguments can be passed as a dictionary    
    print(kwargs) 
    print(type(kwargs)) # dictionary 

add(a=1, b=2, c=3, d=4, e=5) 



# example - 
def add(*args, **kwargs) : 
    print(args) 
    print(kwargs) 

add(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5) 