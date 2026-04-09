# list 

"""
Mutable - can change value
Ordered - index based (0 to n-1)
Duplicates are allowed
Hetrogenous - can store diff types of data types together
"""
a = [1, 2, 3]
b = [3, 2, 3]
c = [1, 2, 5.7, True, print()]
d = ["apple", "rawat", "space"] 

print(a)
print(b[2])
print(c[0:3])
print(d)

# access through loop   
for i in range(len(a)) :   # recommended
    print(a[i])

for i in a :               # accessing values so index can't be used (not recommended)
    print(i)


# access through while loop
i = 0
while i < len(a) : 
    print(a[i])
    i += 1



# List methods 
print(dir(list))  # shows all the methods
help(list)        # shows all the methods with description

# append() - adds element to the end of the list
a.append(4)
print(a)

# insert() - adds element at the specified index
a.insert(1, 5)
print(a)

# remove() - removes the first occurrence of the specified element
a.remove(5)
print(a)

# pop() - removes and returns the element at the specified index (default: last element)
a.pop()
print(a)

# clear() - removes all elements from the list
a.clear()
print(a)

# copy() - returns a shallow copy of the list
a.copy()
print(a)

# count() - returns the number of occurrences of the specified element
a.count(5)
print(a)

# extend() - adds elements of an iterable to the end of the list
a.extend([5, 6, 7])
print(a)

# index() - returns the index of the first occurrence of the specified element
a.index(5)
print(a)

# reverse() - reverses the order of the elements in the list
a.reverse()
print(a)

# sort() - sorts the elements of the list
a.sort()
print(a)