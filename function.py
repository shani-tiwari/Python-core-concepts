def hello() : 
    print("hello")

hello()

# function with parameters
def add(a, b) : 
    print(a+b)

add(1, 2)

# function with return value
def sub(a, b) : 
    return a-b

print(sub(1, 2))

# function with default parameters
def mul(a, b=2) : 
    return a*b

print(mul(1, 2))
print(mul(1))

# function with arbitrary parameters
def add(*args) : 
    sum = 0
    for i in args : 
        sum += i
    return sum

print(add(1, 2, 3, 4, 5))

# keyword argument
def hello(name, age) : 
    print(name, age)

hello(name="shani", age=20)
hello(age=20, name="shani")

# function with arbitrary keyword parameters
def add(**kwargs) : 
    sum = 0
    for i in kwargs : 
        sum += kwargs[i]
    return sum

print(add(a=1, b=2, c=3, d=4, e=5))

# lambda function
add = lambda a, b : a+b
print(add(1, 2))

# recursive function
def fact(n) : 
    if n == 1 : 
        return 1
    else : 
        return n*fact(n-1)

print(fact(5))