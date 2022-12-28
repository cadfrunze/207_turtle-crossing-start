from turtle import Turtle
import time
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Afisare, modificare scor"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.scor = 1
        self.print_scor()

    def print_scor(self):
        self.goto(x=0, y=250)
        self.write(arg=f'Level:{self.scor}', align='Center', move=False, font=FONT)

    def modify_scor(self):
        self.clear()
        self.scor += 1
        self.clear()
        self.print_scor()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg='Lost!', align='Center', move=False, font=FONT)
        time.sleep(1)
        self.clear()
        self.print_scor()

