print("Welcome!\nHere you can check weather a year is leap or not !")
year=int(input("Kindly enter a year:\n"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year!")
        else:
            print("Not leap!")
    else:
        print("Leap year!")
else:
    print("Not leap!")