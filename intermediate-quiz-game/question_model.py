class QuestionModel:
    def __init__(self):
        self.question=0
        self.answer=""
        self.score=0

    def next_question(self,data):
        self.answer=data[self.question]["answer"]
        print(f"{data[self.question]['text']}")
        self.question += 1
    def check_ans(self,user_ans):
        if self.answer==user_ans:
            self.score+=1
            return True
        else:
            return False