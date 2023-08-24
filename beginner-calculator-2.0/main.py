from art import logo


def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2



operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


print(logo)
print("Welcome to the Calculator!")
calc=True
num1=int(input("Enter first number:\n"))
while calc:
    num2=int(input("Enter another number:\n"))
    symbol=input("Enter +,-,*,/:\n")
    for key in operations:
        if key==symbol:
            ans=operations[key]
            num1=(ans(num1=num1,num2=num2))
            print(num1)
    another_input=input("Do you want to continue?\n").lower()
    if another_input=="No":
        calc=False
