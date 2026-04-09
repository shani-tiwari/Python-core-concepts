
'''
    t[0] = 10
    print(t)    # tuple is immutable
    can have duplicates
    accessed in indexed/ordered
    cannot be changed       
    hetrogenous - can have different data types
'''

t = (1, 2, 3, 4, 5)   # tuple

# tuple unpacking
a, b, c, d, e = t
print(a)
print(b)
print(c)
print(d)
print(e)

#  methods
t.index(4)
t.count(4)

a = (1)  # type - int   - unpacking happened auto
a = (1,) # type - tuple - single element tuple