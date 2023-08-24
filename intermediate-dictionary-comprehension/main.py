# names=['shailesh','arnav','raghav','sheetal']
# import random
# student_scores={name:random.randint(1,100) for name in names}
# passed_students={name:score for (name,score) in student_scores.items() if score>30}
# print(passed_students)

# sentence = "what is the velocity of unladen swallow?"
# result={name:len(name) for name in sentence.split()}
#
#
# print(result)

temperatures = {
    'Monday': 22,
    'Tuesday': 18,
    'Wednesday': 25,
    'Thursday': 20,
    'Friday': 23,
    'Saturday': 28,
    'Sunday': 24
}

temperatures_f={day:(temp*9/5)+32 for (day,temp) in temperatures.items()}
print(temperatures_f)