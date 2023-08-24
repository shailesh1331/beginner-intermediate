print("Welcome to the program! You can check weather a number is prime or not!")
number=int(input("Enter a number to check prime\n"))
if number==0:
    print("Not Prime!")
elif number==1 or number==2:
    print("Prime number!")
else:
    for x in range(3,number-1):
        if number%x==0:
            print("Not prime")
            break
        else:
            print("Prime!")
            break