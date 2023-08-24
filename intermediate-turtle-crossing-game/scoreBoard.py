from turtle import Turtle

SCORE=0
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,180)
        self.color('purple')
        self.score=SCORE
        self.write(f'Score:{self.score}',align='center')

    def game_over(self):
        self.goto(0,0)
        self.write(f'Score:{self.score}', align='center')

    def update_score(self):
        self.clear()
        self.write(f'Score:{self.score}', align='center')