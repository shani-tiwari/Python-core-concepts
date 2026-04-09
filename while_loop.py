'''
    a = 1
    while a<=5 : 
        print(a)
        a += 1
'''
# seprate each digit of a number and print it on the new line
'''
    a = 123456
    while a>0 : 
        print(a%10)
        a //= 10    
'''

# reverse a number (can check for palindrome)
'''
    a = 123456
    rev = 0
    while a>0 : 
        rev = rev*10 + a%10
        a //= 10
    print(rev)
'''

# sum of digits of a number
'''
    a = 123456
    sum = 0
    while a>0 : 
        sum += a%10
        a //= 10
    print(sum)
''' 