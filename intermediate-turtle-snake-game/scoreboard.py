from turtle import Turtle
from food import Food

SCORE=0

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.write(f"SCORE:{SCORE}", move=False, align='center')
        self.score=0

    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"SCORE:{self.score}", move=False, align='center')

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!\nSCORE:{self.score}", move=False, align='center')