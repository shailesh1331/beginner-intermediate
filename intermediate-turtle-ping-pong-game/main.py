import time
import turtle
from players import Players
from ball import Ball
from score_board import ScoreBoard

screen = turtle.Screen()
screen.setup(width=900, height=500)
screen.bgcolor('black')
screen.tracer(0)

players1 = Players((-400, 0), color='red')
players2 = Players((400, 0), color='blue')
ball = Ball()
players1_scores = ScoreBoard(1)
players2_scores = ScoreBoard(2)

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    screen.listen()
    screen.onkeypress(players1.up, "w")
    screen.onkeypress(players1.down, "s")
    screen.onkeypress(players2.up, "Up")
    screen.onkeypress(players2.down, "Down")
    ball.move()

    if players1.distance(ball.xcor(), ball.ycor()) <= 35 or players2.distance(ball.xcor(), ball.ycor()) <= 35:
        ball.bounce2()
    elif ball.xcor() > 450:
        ball.reset_ball()
        ball.bounce2()
        players1_scores.update_scores()
        time.sleep(0.1)
    elif ball.xcor() < -450:
        ball.reset_ball()
        ball.bounce2()
        players2_scores.update_scores()
        time.sleep(0.2)

screen.exitonclick()
