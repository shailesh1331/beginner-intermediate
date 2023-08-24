import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
colors = ["red", "yellow", "green", "blue", "maroon"]
turtles = []
positions = [(-260, -120), (-260, -60), (-260, 0), (-260, 60), (-260, 120)]
speeds = [5, 15]

for x in range(len(colors)):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[x])
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.goto(positions[x])
    turtles.append(new_turtle)

choice = screen.textinput("Hello user", prompt="On which color do you want to bet?").lower()
game_on = True

while game_on:
    for player in turtles:
        player.forward(random.choice(speeds))
        if player.xcor() > 280:
            game_on = False
            print(f"{player.color()[0]} has won")
            if player.color()[0] == choice:
                print("Congrats!")
            else:
                print("Omphoo!")

screen.exitonclick()
