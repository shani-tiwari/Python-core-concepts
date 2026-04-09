# dictionary - hashmap 
'''
    mutable
    ordered
    hetrogenous
    key - immutable
    value - mutable
'''

d = {
    "name"   : "shani", 
    "age"    : 20, 
    "gender" : "male"
}

d["name"] # key
d["age"]  # value

d["name"] = "lucky" # update 
d["city"] = "delhi" # add - if key already exists then update else add

d.pop("age")        # remove
d.popitem()         # remove last item
d.clear()           # remove all
d.update({"name" : "jerry", "age" : 24}) # update 
d.get("name")       # get value

d.keys()            # get keys
d.values()          # get values
d.items()           # get key-value pairs


# traversing / loop 
for i in d : 
    print(i) # keys

for i in d.values() : 
    print(i) # values

for i in d.items() : 
    print(i) # key-value pairs


# deep copy vs shallow copy 
d1 = {"name": "shani", "age": 20, "gender": "male"}
d2 = d1         # shallow copy
d3 = d1.copy()  # deep copy

d2["name"] = "lucky"
d3["name"] = "jerry"

print(d1)
print(d2)
print(d3)