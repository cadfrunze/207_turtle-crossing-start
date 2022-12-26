from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Afisare, modificare scor"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.scor = 0
        self.goto(x=0, y=250)
        self.print_scor()

    def print_scor(self):
        self.write(arg=f'Level: {self.scor}', align='Center', move=False, font=FONT)

    def modify_scor(self):
        self.scor += 1
        self.clear()
        self.print_scor()
