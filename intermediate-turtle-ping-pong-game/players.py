from turtle import Turtle


class Players(Turtle):
    def __init__(self,position,color):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.color(color)
        self.goto(position)
        self.score=0


    def up(self):
        new_x=self.xcor()
        new_y=self.ycor()+15
        if new_y<220:
            self.goto(new_x,new_y)

    def down(self):
        new_x=self.xcor()
        new_y=self.ycor()-15
        if new_y>-210:
            self.goto(new_x,new_y)

