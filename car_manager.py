from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(90)
        self.create_car()

    def create_car(self):
        random_num = random.randint(1, 10)
        self.color(random.choice(COLORS))
        self.goto(x=310, y=-250 + (random_num * 50))
        self.move()

    def move(self):
        print(self.xcor())
        self.goto(x=self.xcor() - MOVE_INCREMENT, y=self.ycor())
        if self.xcor() < -300:
            self.create_car()
