print("Welcome to Highscore program!")
scores=[67,87,45,76,87,87,98,45,86,76,66,99,54]
highest=0
for x in range(0,len(scores)):
    if scores[x]>highest:
        highest=scores[x]
print(f"Highest score is {highest}")