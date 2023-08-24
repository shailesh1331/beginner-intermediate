from turtle import Turtle
import random

CARS=[]
CAR_COLORS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 0.5, 0), (0.5, 0, 1), (0, 0.5, 1), (0.5, 1, 0), (1, 0.5, 0.5), (0.5, 1, 0.5), (0.5, 0.5, 1), (1, 1, 0.5), (1, 0.5, 1), (0.5, 1, 1), (0, 0, 0), (1, 1, 1)]

class Traffic(Turtle):
    def __init__(self):
        super().__init__()
        self.create_cars()
        self.cars=CARS

    def create_cars(self):
        for _ in range(10):
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.color(random.choice(CAR_COLORS))
            new_car.penup()

            # Generate random coordinates for the new car
            x = random.randint(-400, 450)
            y = random.randint(-140, 140)

            new_car.goto(x, y)

            # Check for collisions with existing cars
            collision = True
            while collision:
                collision = False
                for car in CARS:
                    if new_car.distance(car) <60:  # Adjust the distance as needed
                        collision = True
                        x = random.randint(0, 400)
                        y = random.randint(-140, 140)
                        new_car.goto(x, y)
                        break
            CARS.append(new_car)

    def is_beyond_boundary(self, car):
        return car.xcor() < -400

    def reset_car(self, car):
        car.goto(400, car.ycor())

    def move_cars(self):
        for car in self.cars:
            car.forward(-10)
            if self.is_beyond_boundary(car):
                self.reset_car(car)

