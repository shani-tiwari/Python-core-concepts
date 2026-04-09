
s = {1, 2, 3, 4, 5}
'''
mutable
No duplicates
Unordered
Semi-Hetrogenous - can have different data types but not nested
'''

s[2] # not subscriptable

# set operations

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s1.add(6)
s2.remove(6)
s2.discard(6) # no error if element not found
s2.pop() # removes random element(or smallest one with hash value)
s2.clear() # removes all elements

# between two sets
s1.union(s2)                # s1 | s2
s1.intersection(s2)         # s1 & s2
s1.difference(s2)           # s1 - s2
s1.symmetric_difference(s2) # s1 ^ s2
s1.issubset(s2)             # s1 <= s2
s1.issuperset(s2)           # s1 >= s2
s1.isdisjoint(s2)           # no common elements

# traversing / loop 
for i in s : 
    print(i) # not ordered

# frozen set - immutable version of set
fs = frozenset(s)
fs[2] # subscriptable
