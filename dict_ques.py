# count the frequency of all elements
a = [1, 2, 1, 2, 1, 2, 3, 3, 3, 5]
d = {} 
for i in a : 
    if i in d : 
        d[i] += 1
    else :
        d[i] = 1
print(d)


# remove duplicate elements 
a = [1, 2, 1, 2, 1, 2, 3, 3, 3, 5]
print(list(set(a)))

# merge two dictionaries 
d1 = {"name": "shani", "age": 20}
d2 = {"gender": "male", "city": "delhi"}
d1.update(d2)
print(d1)

