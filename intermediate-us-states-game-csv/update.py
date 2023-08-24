from turtle import Turtle

class Update(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.speed('fastest')

    def update_data(self,x,y,element):
        self.goto(x,y)
        self.write(f'{element}',move=False)