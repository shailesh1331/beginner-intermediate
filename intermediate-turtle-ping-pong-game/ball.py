from turtle import Turtle

X=8
Y=8
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.shape('circle')
        self.shapesize(1)
        self.color('yellow')
        self.goto(0,0)

    def move(self):
        new_x=self.xcor()+Y
        new_y=self.ycor()+X
        if new_y<250 and new_y>-250:
            self.goto(new_x,new_y)
        else:
            self.bounce()
    def bounce(self):
        global X
        X = X*-1
        new_x = self.xcor()+Y
        new_y = self.ycor() +X
        self.goto(new_x, new_y)

    def bounce2(self):
        global Y
        Y = Y*-1

    def reset_ball(self):
        self.goto(0, 0)
