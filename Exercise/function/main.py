#   Declare a function named reverse_list. It takes an array as a parameter, and print reverse array
"""def reverse_list(arg) : 
    # start from last index and go to first index with step -1
    for i in range(len(arg)-1, -1, -1) : 
        print(arg[i])
    # another way
    print(arg[::-1])

reverse_list([1, 2, 3, 4, 5])
reverse_list(['A', 'B', 'C'])"""


# function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
"""def capitalize_list_items(arg) : 
    new = []
    for i in arg : 
        new.append(i.capitalize())
    return new

print(capitalize_list_items(['apple', 'banana', 'cherry']))"""


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
"""def add_item(arg, item) : 
    arg.append(item)
    # arg.remove(item)
    return arg

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))     

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5)) """


#  takes a parameter and it checks if it is empty or not
"""def is_empty(arg) : 
    if arg == [] : 
        print("Empty")
    else : 
        print("Not Empty")

is_empty([])
is_empty([1, 2, 3])"""


#   Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
"""def show_args(**kwargs) : 
    for key, value in kwargs.items() : 
        print(key, value)

show_args(name="John", age=30, city="New York")"""


#   Write a functions which checks if all items are unique in the list.
"""def is_unique(arg) : 
    for i in arg : 
        if arg.count(i) > 1 : 
            return False
    return True

print(is_unique([1, 2, 3, 4, 5]))
print(is_unique([1, 2, 3, 4, 4]))"""


#  Write a function that takes a list of numbers and returns the sum of all the numbers in the list.
"""def sum_list(arg) : 
    total = 0
    for i in arg : 
        total += i
    return total

print(sum_list([1, 2, 3, 4, 5]))"""


#  function which checks if all the items of the list are of the same data type.
"""def is_same_type(arg) : 
    for i in arg : 
        if type(i) != type(arg[0]) : 
            return False
    return True

print(is_same_type([1, 2, 3, 4, 5]))
print(is_same_type([1, 2, 3, 4, 4]))"""


#   function which check if provided variable is a valid python variable
"""def is_valid_variable(arg) : 
    if arg.isidentifier() : 
        return True
    else : 
        return False

print(is_valid_variable("name"))
print(is_valid_variable("name"))"""



