from turtle import Screen
import time
from create_snake import Create_Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.screensize(canvwidth=600, canvheight=300, bg='black')
screen.tracer(0)

snake = Create_Snake()
scoreboard = ScoreBoard()

food = Food()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
    screen.listen()
    screen.onkey(snake.turn_up, "Up")
    screen.onkey(snake.turn_down, "Down")
    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.turn_right, "Right")
    for segments in snake.snake:
        if food.distance(segments.xcor(), segments.ycor()) < 18:
            food.refresh()
            scoreboard.score+=1
            scoreboard.update_score()
            snake.add_segment()

    if snake.snake[0].xcor() > 300 or snake.snake[0].xcor() < -280 or\
            snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
        snake.reset()
        snake=Create_Snake()
        scoreboard.reset()

    for segment in snake.snake:
        if segment == snake.snake[0]:
            pass
        elif snake.snake[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
