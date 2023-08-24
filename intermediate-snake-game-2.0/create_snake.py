from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE=[]

class Create_Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake = SNAKE
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.goto(position)
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.penup()
            self.snake.append(new_segment)

    def move_forward(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(20)

    def turn_up(self):
        if self.snake[0].heading() != 270 and self.snake[0].heading() != 90:
            self.snake[0].setheading(90)

    def turn_down(self):
        if self.snake[0].heading() != 270 and self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def add_segment(self):
        last_segment = self.snake[-1]
        new_segment = Turtle()
        new_segment.goto(last_segment.xcor(),last_segment.ycor())
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        self.snake.append(new_segment)

    def turn_left(self):
        if self.snake[0].heading() != 0 and self.snake[0].heading() != 180:
            self.snake[0].setheading(180)

    def turn_right(self):
        if self.snake[0].heading() != 0 and self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)  # Move the segment out of the screen
            segment.clear()  # Clear the segment from the screen
        self.snake.clear()  # Clear the snake list
        self.create_snake()
