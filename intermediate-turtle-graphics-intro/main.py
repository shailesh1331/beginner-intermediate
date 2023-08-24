#####Turtle Intro######

import turtle as t
from turtle import Screen
timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# for x in range(0,100):
#     timmy_the_turtle.forward(5)
#     if x%2==0:
#         timmy_the_turtle.penup()
#     else:
#         timmy_the_turtle.pendown()

# sides=3
# degree=360
# for x in range(0,5):
#     for y in range(0,sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/sides)
#     sides+=1

######## Challenge 1 - Draw a spirograph   ###############
screen=Screen()
timmy_the_turtle.right(10)


for x in range(0,72):
    timmy_the_turtle.speed('fastest')
    timmy_the_turtle.circle(100)
    timmy_the_turtle.right(5)


screen.exitonclick()