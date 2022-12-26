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
scorul = Scoreboard()


def move_up():
    playerul.move_up()


def move_down():
    if playerul.ycor() <= -280:
        screen.onkey(key='Up', fun=move_up)
    else:
        playerul.move_down()


def move_left():
    if playerul.xcor() <= -280:
        screen.onkey(key='Down', fun=move_down)
    else:
        playerul.move_left()


def move_right():
    if playerul.xcor() >= 280:
        screen.onkey(key='Left', fun=move_left)
    else:
        playerul.move_right()


screen.onkey(key='Up', fun=move_up)
screen.onkey(key='Down', fun=move_down)
screen.onkey(key='Left', fun=move_left)
screen.onkey(key='Right', fun=move_right)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    screen.update()
    car.move_cars()
    if playerul.ycor() >= 240:
        screen.tracer(0)
        scorul.modify_scor()
        playerul.finish_line()
        screen.update()
