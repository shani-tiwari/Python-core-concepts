# higher order funciton  --- map, filter, reduce

#  Use filter to filter out countries containing 'land'.
countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Denmark', 'Finland']
# explain - 
# filter is used to filter out countries containing 'land'
# lambda country: 'land' not in country is a lambda function that checks if 'land' is not in the country
# list() is used to convert the filter object to a list
filtered = list(filter(lambda country: 'land' in country, countries))


# Use filter to filter out countries having exactly six characters.
filtered = list(filter(lambda country: len(country) == 6, countries))


# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
numbers = [1, 2, 3, 4, 5, 6, 7 , 8, 9]
chain = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))


# Use reduce to sum all the numbers in the numbers list.
import functools as ft
res = ft.reduce(lambda x, y: x + y, [1, 2, 3])


# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
res = ft.reduce(lambda x, y: x + ", " + y, countries)

# Create a function returning a dictionary, 
# where keys stand for starting letters of countries and values are the number of country names starting with that letter.
dict = {}
for i in countries : 
    if i[0] in dict : 
        dict[i[0]] += 1
    else : 
        dict[i[0]] = 1

