# try - except - else - finally 

a = int(input("enter a number : "))

try : 
    print(10 / a)
except ZeroDivisionError : 
    print("cannot divide by zero")
except ValueError : 
    print("invalid input")
except Exception as e : 
    print(e)
else : 
    print("no exception")
finally : 
    print("always execute")


# raise --- manually raise exception 
raise ValueError("invalid input")


# custom exception 
class MyException(Exception) : 
    def __init__(self, message) : 
        self.message = message

try : 
    raise MyException("invalid input")
except MyException as e : 
    print(e) 


