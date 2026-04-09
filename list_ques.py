# print positive and negative elements of an list
"""
    l = [1, 2, 3, -1, -2, -3, 0]

    for i in l : 
        if i > 0 : 
            print(f"{i} is positive")
        elif i < 0 : 
            print(f"{i} is negative")
        else : 
            print(f"{i} is zero")    
"""

# Mean of list elements 
l = [1, 2, 3, 4, 5]

mean = sum(l) / len(l)
print(mean)


#   remove duplicates from list
'''
    l = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 6, 8, 9, 8, 10, 9, 10]

    for i in l : 
        if i in l : 
            l.remove(i)
    print(l)
'''

# find the greatest element of list
'''
    l = [1, 2, 3, 4, 5]

    greatest = l[0] 

    for i in l : 
        if i > greatest : 
            greatest = i

    print(greatest) 
'''

# second largest number of list
'''
    l = [1, 2, 3, 4, 5]

    first_largest  = l[0]
    second_largest = l[0] 

    for i in l : 
        if i > first_largest :
            second_largest = first_largest
            first_largest = i
        elif i > second_largest and i != first_largest :
            second_largest = i

    print(second_largest) 
''' 

# check list is sorted or not
'''
    l = [1, 2, 3, 4, 5]

    for i in range(len(l) - 1) : 
        if l[i] > l[i+1] :         # index out of range error
            print("List is not sorted")
            break
    else : 
        print("List is sorted")
'''