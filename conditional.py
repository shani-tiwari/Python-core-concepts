# if else
# indentation is must(5 spaces or 1 tab)

if 10 == 10 :
    print("equal")
else :
    print("unequal")

# if elif else

if 10 == 10 :
    print("equal")  
elif 10 == 11 :
    print("equal")
else :
    print("unequal")

# nested if else

if 10 == 10 :
    print("equal")
    if 10 == 10 :
        print("equal")
    else :
        print("unequal")
else :
    print("unequal")

# ternary operator
print("equal" if 10 == 10 else "unequal")


# assert --- check condition 
a = int(input("enter a number : "))
assert a > 0, "a is not greater than 0"


# pass --- do nothing 
if 10 == 10 :
    pass
else :
    print("unequal")
