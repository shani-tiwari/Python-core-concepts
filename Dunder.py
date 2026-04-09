# dunder methods --- double underscore methods 
# also called as magic methods 
# used to implement operator overloading 
# customize behaviour of your class
# auto called when u perform certain action on an object

# example - 
# __init__
# __str__
# __add__
# __sub__
# __mul__
# __truediv__
# __len__
# __getitem__
# __setitem__
# __delitem__
# __call__
# __eq__
# __ne__
# __lt__
# __le__
# __gt__
# __ge__

# example - 
class Calculator : 
    def __init__(self, a, b) : 
        self.a = a 
        self.b = b 
    def __add__(self, other) : 
        return self.a + self.b + other.a + other.b #
    def __sub__(self, other) : 
        return self.a - self.b - other.a - other.b 
    def __mul__(self, other) : 
        return self.a * self.b * other.a * other.b 
    def __truediv__(self, other) : 
        return self.a / self.b / other.a / other.b 
    def __len__(self) : 
        return self.a + self.b 
    def __getitem__(self, key) : 
        return self.a + self.b + key 
    def __setitem__(self, key, value) : 
        self.a = value 
        self.b = value 
    def __delitem__(self, key) : 
        del self.a 
        del self.b 
    def __call__(self) : 
        return self.a + self.b 
    def __eq__(self, other) : 
        return self.a == other.a and self.b == other.b 
    def __ne__(self, other) : 
        return self.a != other.a or self.b != other.b 
    def __lt__(self, other) : 
        return self.a < other.a and self.b < other.b 
    def __le__(self, other) : 
        return self.a <= other.a and self.b <= other.b 
    def __gt__(self, other) : 
        return self.a > other.a and self.b > other.b 
    def __ge__(self, other) : 
        return self.a >= other.a and self.b >= other.b 

call = Calculator(1, 2) 
print(call + Calculator(3, 4)) 
print(call - Calculator(3, 4)) 
print(call * Calculator(3, 4)) 
print(call / Calculator(3, 4)) 
print(len(call)) 
print(call[5]) 
call[6] = 7 
print(call.a, call.b) 
del call.a 
del call.b 
print(call()) 
print(call == Calculator(3, 4)) 
print(call != Calculator(3, 4)) 
print(call < Calculator(3, 4)) 
print(call <= Calculator(3, 4)) 
print(call > Calculator(3, 4)) 
print(call >= Calculator(3, 4)) 