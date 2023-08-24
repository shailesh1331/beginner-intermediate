height=float(input("Enter your height in meters:\n"))
weight=float(input("Enter your weight in kgs:\n"))
bmi=(weight/(height*height)).__round__(2)
print(bmi)
if bmi<18.5:
    print("You are underweight!")
elif bmi<25:
    print("You have normal weight!")
elif bmi<30:
    print("You are overweight!")
elif bmi<35:
    print("You are obese!")
else:
    print("You are clinically obese!")
