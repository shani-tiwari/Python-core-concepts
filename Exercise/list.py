#  Filter only negative and zero in the list using list comprehension
# l = [-1, 0, 1, 2, -2, 3, -3, 4, -4, 5, -5]
# print([i  for i in l if i <= 0])
"""for i in l : 
    if i <= 0 : 
        print(i)"""


#  Flatten a nested list using list comprehension
l = [[1, 2, 3], 4, 0, [4, 5, 6], [7, 8, 9]]
# explain - 
# x is the outer loop that iterates through the list l
# item is the inner loop that iterates through the list x
# (x if isinstance(x, list) else [x]) is a conditional expression that checks if x is a list
# if x is a list, it iterates through the list x
# if x is not a list, it iterates through the list [x]
flattened = [item   for x in l   for item in (x if isinstance(x, list) else [x])]


# Using list comprehension create the following list of tuples:
"""[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]"""
# explain - 
# i is the outer loop that iterates through the range(11)
# 1 is the second loop that iterates through the range(1)
# *[i**j for j in range(0, 6)] is a conditional expression that checks if i is a list
# if i is a list, it iterates through the list i
# if i is not a list, it iterates through the list [i]
tuples = [(i, 1, *[i**j for j in range(0, 6)]) for i in range(11)]


#  Change the following list to a list of dictionaries:
"""countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]



#  Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [f"{country} {city}"   for sublist in names   for country, city in sublist]


#  Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2 : (y2 - y1) / (x2 - x1)
y_intercept = lambda x1, y1, x2, y2 : y1 - slope(x1, y1, x2, y2) * x1

print(slope(1, 2, 3, 4))
print(y_intercept(1, 2, 3, 4))