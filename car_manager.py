from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.ran_nr = 10
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        random_sansa = random.randint(1, self.ran_nr)
        if random_sansa == 1:
            car = Turtle('square')
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            y_cor = random.randint(-250, 220)
            car.goto(x=300, y=y_cor)
            self.all_cars.append(car)

    def move_cars(self):
        for move in self.all_cars:
            move.backward(self.car_speed)

    def level_up(self):
