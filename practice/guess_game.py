import random 

num = random.randint(1, 10)

guess = 0
tries = 0

while guess != num : 
    guess = int(input(" guess : "))
    tries += 1
    if guess < num : 
        print(" too low")
    elif guess > num : 
        print(" too high")
    else : 
        print(" correct")
        print(f" you took {tries} tries")