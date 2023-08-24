from art import logo
import os

def compare(dictionary):
    highest=0
    for x in range(1,len(dictionary)+1):
        if dictionary[f'{x}'][1]>highest:
            highest=dictionary[f'{x}'][1]
    for x in range(1,len(dictionary)+1):
        if dictionary[f'{x}'][1]==highest:
            print(f"{dictionary[f'{x}'][0]} is the winner")



print(logo)
print("Welcome to secret auction program!")
auction=True
data={}
key=1
name=input("Enter your name!:\n")
bid=int(input("Enter your bid amount:\n"))
data[f"{key}"]=[name,bid]
os.system('cls')
while auction:
    name=input("Enter Your name!:\n")
    bid = int(input("Enter your bid amount:\n"))
    key+=1
    data[f"{key}"] = [name,bid]
    another_user=input("Is there any other person to bid?\n").lower()
    if another_user=="no":
        compare(data)
        auction=False
    elif another_user=="yes":
        os.system('cls')
