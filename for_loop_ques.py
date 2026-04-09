# accept int, print n times 
'''
    n = int(input(" number : "))
    for i in range(n) :
        print("hello") 
'''

# print nartural number upto n
'''
    n = int(input(" number : "))
    for i in range(n) :
        print(i+1)
'''

# reverse for loop, n to 1
'''
    n = int(input(" number : "))
    for i in range(n, 0, -1) : 
        print(i)
'''

# print a table
'''
    n = int(input(" number : "))
    for i in range(n, n*10+1, n) : 
        print(i)
'''

# sum upto n terms
'''
    n = int(input(" number : "))
    sum = 0
    for i in range(1, n+1) : 
        sum += i
    print(f" sum = {sum}", end="\n")
'''

# sum of first n even numbers
'''
    n = int(input(" number : "))
    sum = 0
    for i in range(2, n+1, 2) : 
        sum += i
    print(f" sum = {sum}", end="\n")
'''

# factorial of a number 
'''
    n = int(input(" number : "))
    fact = 1
    for i in range(n, 0, -1) : 
        fact *= i

    print(f" factorial = {fact}", end="\n")
'''

# fibonacci series
'''
    n = int(input(" number : "))
    a = 0
    b = 1
    for i in range(n) : 
        print(a)
        c = a + b
        a = b
        b = c
'''

# print sum of all even & odd numbers in a range seprately
'''
    n = int(input(" number : "))
    Esum = 0
    for i in range(2, n, 2) :
        Esum += i
    print(f"even sum = {Esum}")

    Osum = 0
    for i in range(1, n, 2) :
        Osum += i
    print(f"odd sum = {Osum}")
'''

# check number is perfect number or not
'''
    n = int(input(" number : "))
    sum = 0
    for i in range(1, n) :
        if n%i == 0 :
            sum += i
    if sum == n :
        print("perfect number")
    else :
        print("not a perfect number")
'''

# print table of n in reverse order
'''
    n = int(input(" number : "))
    for i in range(n*10, 0, -n) : 
        print(i)
'''

# check number is prime or not 
'''
    n = int(input(" number : "))
    for i in range(2, n) :
        if n%i == 0 :
            print("not a prime number")
            break
    else :
        print("prime number")
'''

# reverse string without in build functions
'''
    s = "shani"
    for i in range(len(s), 0, -1) : 
        print(s[i-1], end="")
'''

# count vowels & consonants in a string
'''
    s = input(" string : ")
    vowels = 0
    consonants = 0
    for i in s : 
        if i in "aeiouAEIOU" : 
            vowels += 1
        else : 
            consonants += 1
    print(f" vowels = {vowels}")
    print(f" consonants = {consonants}")
'''

# 