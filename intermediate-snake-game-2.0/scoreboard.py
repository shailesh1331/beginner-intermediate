from turtle import Turtle
file=open('highscore.txt')
contents=int(file.read())
file.close()

SCORE=0

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = contents
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.write(f"SCORE:{SCORE} HIGHSCORE:{self.highscore}", move=False, align='center')
        self.score=0

    def update_score(self):
        self.clear()
        self.write(f"SCORE:{self.score} HIGHSCORE:{self.highscore}", move=False, align='center')


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        with open('highscore.txt',mode='w') as file:
            file.write(f"{self.highscore}")
        self.score=0
        self.update_score()
    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!\nSCORE:{self.score}", move=False, align='center')
    #