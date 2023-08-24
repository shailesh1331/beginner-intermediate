from data import question_data
from question_model import QuestionModel

data=question_data
question_model=QuestionModel()
for x in range(0,len(data)-1):
    question_model.next_question(data)
    user_ans=input("True/False:").title()
    check=question_model.check_ans(user_ans)
    if check==True:
        print("Correct")
        print(f"Score:{question_model.score}/{question_model.question}")
    else:
        print("Wrong")
        print(f"Score:{question_model.score}/{question_model.question}")
