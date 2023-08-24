from turtle import Turtle


class Player(Turtle):
    def __init__(self,color):
        super().__init__()
        self.shape('turtle')
        self.color(color)
        self.penup()
        self.goto(0,-180)
        self.setheading(90)

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(5)


