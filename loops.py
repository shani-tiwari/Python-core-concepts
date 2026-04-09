# for & while 
# range --- range(start,stop,step) --- range(0, 5, 1) --- stop is exclusive

# for loop - works on iterables (string,list,tuple,dict,set)    
for i in range(5) : # range(0, 5, 1) --- default values are 0, _, 1
    print(i)

# while loop - works on condition
i = 0
while i < 5 :
    print(i)
    i += 1


# for loop with else
for i in range(5) :
    print(i)
else :
    print("loop completed")


# while loop with else
i = 0
while i < 5 :
    print(i)
    i += 1
else :
    print("loop completed")


# break - exit loop
for i in range(5) :
    # conditional break loop
    if i == 3 :
        break
    print(i)

# continue - skip iteration
for i in range(5) :
    # conditional skip iteration
    if i == 3 :
        continue
    print(i)

# pass - do nothing
for i in range(5) :
    # conditional do nothing when in other some logic performed
    if i == 3 :
        pass
    print(i)


# nested loop
for i in range(5) :
    for j in range(i) :
        print(j, end=" ")
    print()


# pattern printing
for i in range(5) :
    for j in range(i) :
        print("*", end=" ")
    print()
