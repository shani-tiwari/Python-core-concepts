# input 2 number print greatest 
'''
    first = int(input("first number : "))
    second = int(input("second number : "))

    if first > second : 
        print(f"1st no. {first} is greatest")
    else : 
        print(f"2nd no. {second} is greatest")
'''

# input gender and print greeting dynamically
'''
    gender = input(" Gender : ").lower()
    if gender == "male" : 
        print("good morning sir")
    elif gender == "female" :
        print("hello mam ")
    else :
        print("invalid gender")
'''

# input int, check even odd
'''
    a = int(input(" number : "))
    if a%2 == 0 :
        print("even")
    else :
        print("odd")
'''

# input name & age, check valid voter
'''
    name = input(" Name : ")
    age = int(input(" age : "))
    if age >= 18 :
        print(f"hey {name}, u r a valid voter")
    else :
        print(f"hey {name}, u r not a valid voter")
'''

# leap year 
'''
    year = int(input(" enter year : "))
    if year%400 == 0 and year%100 == 0 :
        print("leap year")
    elif year%100 != 0 and year%4 == 0 :
        print("leap year")
    else :
        print("not a leap year")
'''
