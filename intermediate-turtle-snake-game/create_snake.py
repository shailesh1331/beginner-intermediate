from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class SnakeSegment(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()


class Create_Snake:
    def __init__(self):
        self.snake = []
        self.create()

    def create(self):
        for position in STARTING_POSITIONS:
            new_segment = SnakeSegment()
            new_segment.goto(position)
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
        new_segment = SnakeSegment()
        new_segment.goto(last_segment.position())
        self.snake.append(new_segment)

    def turn_left(self):
        if self.snake[0].heading() != 0 and self.snake[0].heading() != 180:
            self.snake[0].setheading(180)

    def turn_right(self):
        if self.snake[0].heading() != 0 and self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
