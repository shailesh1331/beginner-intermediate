MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coffee(data1,data2):
    for key in data1:
        for keyy in data2:
            if key==keyy and data1[key]>data2[keyy]:
                data1[key]=data1[key]-data2[keyy]
            elif keyy==key and data1[key]<data2[keyy]:
                return False
    return True


def process_coins(c1,c2,c3,c4,price):
    c1=c1*0.25
    c2=c2*0.10
    c3=c3*0.05
    c4=c4*0.01
    total=c2+c4+c3+c1
    if total>price:
        print(f"Here's the change: {(total-price).__round__(2)}")
    else:
        print(f"insufficient coins!{total} here's the return!")



machine=True
while machine:
    choice=input("What would you like to have? espresso/latte/capuccino:\n")
    if choice in MENU:
        for key in MENU:
            if key==choice:
                select=MENU[f"{key}"]
        coins1=int(input("how many quaters?:"))
        coins2 = int(input("how many dimes?:"))
        coins3 =int( input("how many nickles?:"))
        coins4 =int( input("how many pennies?:"))
        process_coins(coins1,coins2,coins3,coins4,select["cost"])
        check=process_coffee(resources,select["ingredients"])
        if check==True:
            print(f"Here's your coffee. ☕ enjoy!")
            machine=input("Do you want to have more ?").lower()
            if machine=="no":
                machine=False
        else:
            print(f"Insufficient resources! Here's Your return {(coins1*0.25)+(coins2*0.10)+(coins3*0.05)+(coins4*0.1)}")
            machine=False
    else:
        print("There's no such option!")
