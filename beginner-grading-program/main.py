student_scores={
    "harry":81,
    "ron":78,
    "hermione":61,
    "draco":88,
    "panda":100,
}

student_grades=[]
for key in student_scores:
    if student_scores[key]>90:
        student_grades.append([f"{key}","Outstanding"])
    elif student_scores[key]>80:
        student_grades.append([f"{key}","Excellent"])
    elif student_scores[key]>70:
        student_grades.append([f"{key}","Average"])
    elif student_scores[key]<70:
        student_grades.append([f"{key}","Below Average"])
print("Welcome to the student grading program! Here are the Grades!")
print(student_grades)