import time
from turtle import Turtle, Screen
from player import Player
from scoreBoard import ScoreBoard
from traffic import Traffic

screen = Screen()
screen.setup(width=800,height=400)
screen.bgcolor('black')
screen.tracer(0)
prompt=Screen()
text=prompt.textinput('Welcome to the game!','Enter your color: Blue/Red/Yellow').lower()
player = Player(text)
score_board=ScoreBoard()
traffic=Traffic()

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    traffic.move_cars()
    screen.listen()
    screen.onkeypress(player.up,"w")
    for car in traffic.cars:
        if player.distance(car.xcor(),car.ycor())<23:
            game_on=False
            score_board.game_over()
    if player.ycor()>145:
        player.goto(0,-180)
        score_board.score+=1
        score_board.update_score()

screen.exitonclick()

