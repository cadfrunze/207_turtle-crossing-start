import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
playerul = Player()
car = CarManager()


def move_up():
    playerul.move_up()


screen.onkey(key='Up', fun=move_up)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()

