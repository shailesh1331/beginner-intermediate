import random

print("Welcome to the coin toss program!\n")
choice=[0,1]
if random.choice(choice)==0:
    print("Its heads!")
else:
    print("Its tails!")