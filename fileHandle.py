# file handling 

# open, close, read, write, append

# modes - 
'''
    r - read
    w - write
    a - append
    x - create
    t - text
    b - binary
'''

# open - (file name, mode)

# read - read, readline, readlines
# write - write, writelines
# close - close


# with - automatically close

with open("file.txt", "w") as f : 
    f.write("hello")

with open("file.txt", "r") as f : 
    print(f.read())
with open(r"C:\Users\shani\Desktop\Python\file.txt") as f : 
    print(f.read())


with open("file.txt", "a") as f : 
    f.write("hello")

# with open("file-2.txt", "x") as f : 
#     f.write("hello")

# ValueError: Must have exactly one of create/read/write/append mode and at most one plus
    # with open("file-2.txt", "t") as f : 
    #     print(f.read())

    # with open("file.txt", "b") as f : 
    #     print(f.read()) 