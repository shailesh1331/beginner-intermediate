from turtle import Turtle,Screen


def move_forward():
    turtle.forward(10)
def move_backward():
    turtle.backward(10)
def turn_left():
    turtle.left(10)
def turn_right():
    turn_right(10)



turtle=Turtle()
screen=Screen()
screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")







screen.exitonclick()