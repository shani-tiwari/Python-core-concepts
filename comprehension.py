
a = 12
print("even" if a % 2 == 0 else "odd") # ternary operator 

# list comprehension - 
a = [1, 2, 3, 4, 5] 
print([i*i for i in a])  

# set comprehension - 
a = {1, 2, 3, 4, 5} 
print({i*i for i in a}) 

# dict comprehension - 
a = {1, 2, 3, 4, 5} 
print({i:i*i for i in a}) 

# generator expression - 
a = {1, 2, 3, 4, 5} 
print((i*i for i in a))     