
# type casting / conversion
a = 10
b = str(a)
print(type(b))  # str

a = 10
b = float(a)
print(type(b))  # float

a = 10
b = int(a)
print(type(b))  # int

a = 10
b = bool(a)
print(type(b))  # bool
"""
falsyy values - [], (), {}, 0, 0.0, "", None, "", "False"
"""

a = 10
b = complex(a)
print(type(b))  # complex

a = 10
b = list(a)
print(type(b))  # list

a = 10
b = tuple(a)
print(type(b))  # tuple

a = 10
b = set(a)
print(type(b))  # set

a = 10
b = dict(a)
print(type(b))  # dict

a = 10
b = None(a)
print(type(b))  # NoneType