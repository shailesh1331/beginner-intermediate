print("Welcome to the pizza order program!")
size=input("Enter the size of pizza you want:\n").lower()
meyonese=input("Do you want meyonese?\n").lower()
pepperoni=input("Do you want pepperoni?\n").lower()
amount=0
if size=="s":
    amount+=10
elif size=="m":
    amount+=20
elif size=="l":
    amount+=30
if meyonese=="yes":
    amount+=11
if pepperoni=="yes":
    amount+=3
print(f"Your bill is {amount}$")