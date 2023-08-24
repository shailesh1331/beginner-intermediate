from turtle import Turtle
from players import Players


class ScoreBoard(Turtle):
    def __init__(self,id):
        super().__init__()
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.shape('circle')
        self.shapesize(1)
        self.color('white')
        self.score=0
        self.id=id
        if id==1:
            self.goto(-50,200)
            self.write(f"player{id} Score:{self.score}", move=False,align='center')
        elif id==2:
            self.goto(50,200)
            self.write(f"player{id} Score:{self.score}",move=False,align='center')

    def update_scores(self):
        self.score+=1
        self.clear()
        self.write(f"player{self.id} Score:{self.score}", move=False, align='center')