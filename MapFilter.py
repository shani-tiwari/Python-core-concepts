# map - apply a function to all items in an iterable , takes a list
# syntax - map(function, iterable) 

# example - 
def square(x) : 
    return x * x 

a = [1, 2, 3, 4, 5] 
print(list(map(square, a))) # list() is used to convert map object to list - [1, 4, 9, 16, 25]



# filter - filter items based on a condition , takes a list
# syntax - filter(function, iterable) 

# example -  
def is_even(x) : 
    return x % 2 == 0 

a = [1, 2, 3, 4, 5] 
print(list(filter(is_even, a))) 



