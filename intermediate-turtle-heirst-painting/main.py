import colorgram
from turtle import Turtle, Screen


def u_turn(turtle):
    if turtle.xcor()>0:
        turtle.left(90)
        turtle.pencolor(colors2[x])
        turtle.dot(size=20)
        turtle.forward(40)
        turtle.left(90)
    else:
        turtle.right(90)
        turtle.pencolor(colors2[x])
        turtle.dot(size=20)
        turtle.forward(40)
        turtle.right(90)



colors1=colorgram.extract("image.jpg",30)
print(colors1)
colors2=[]
for x in range(0,20):
    colors2.append((colors1[x].rgb.r,colors1[x].rgb.g,colors1[x].rgb.b))
print(colors2)
turtle=Turtle()
screen=Screen()
screen.colormode(255)
turtle.hideturtle()
turtle.penup()
turtle.speed('fastest')
turtle.goto(-280,-220)
while turtle.position()<(300.0,220.0):
    for x in range(0,13):
        turtle.pencolor(colors2[x])
        turtle.dot(size=20)
        turtle.forward(40)
    u_turn(turtle=turtle)









screen.exitonclick()
