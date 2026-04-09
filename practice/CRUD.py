from pathlib import Path



print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")


def readFileandFolder() : 
    path = Path(' ') 
    items = list(path.rglob('*'))
    for i, item in enumerate(items) : 
        print(i+1, item)


def createFile() : 
    try : 
        readFileandFolder() 
        choice = input("enter your path : ")
        p = Path(choice)

        if not p.exists() : 
            with open(p, "w") as f : 
                f.write(input("enter your query : "))
        else : 
            print("file already exists")

    except : 
        print("invalid choice")

def readFile() : 
    try : 
        readFileandFolder()
        choice = input("which file u want to read : ")
        p = Path(choice)
        if p.exists() and p.is_file() : 
            with open(p, "r") as f : 
                print(f.read())
        else : 
            print("file not found")
    except : 
        print("invalid choice")

def updateFile() : 
    try : 

        readFileandFolder()
        choice = input("which file u want to update : ")
        p = Path(choice)

        if p.exists() and p.is_file() : 
            print("press 1 for changing name of file")
            print("press 2 for adding content to file")
            print("press 3 for over writing data of file")

            choice = int(input("enter your preference : "))
            if choice == 1 : 
                p.rename(input("enter new name of file : "))
            elif choice == 2 : 
                with open(p, "a") as f : f.write(input("enter your query : "))
            elif choice == 3 : 
                with open(p, "w") as f : f.write(input("enter your new data : "))
            else : 
                print("invalid choice")

        else : 
            print("file not found")

    except : 
        print("invalid choice")

def deleteFile() :
    try : 
        readFileandFolder()
        choice = input("which file u want to delete : ")
        p = Path(choice)
        if p.exists() and p.is_file() : 
            p.unlink()
        else : 
            print("file not found")
    except : 
        print("invalid choice")


#  choice from here 
choice = int(input("enter your choice : "))
if choice == 1   : 
    createFile()
elif choice == 2 :
    readFile()
elif choice == 3 :
    updateFile()
elif choice == 4 : 
    deleteFile()




'''

if choice == 1 : 
    with open("file.txt", "w") as f : 
        f.write(input("enter your name : "))

elif choice == 2 : 
    with open("file.txt", "r") as f : 
        print(f.read())

elif choice == 3 : 
    with open("file.txt", "a") as f : 
        f.write(input("enter your name : "))

elif choice == 4 : 
    with open("file.txt", "w") as f : 
        f.write("") 

else : 
    print("invalid choice") 
'''