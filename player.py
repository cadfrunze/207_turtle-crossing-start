from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 240


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        self.goto(x=self.xcor() - MOVE_DISTANCE, y=self.ycor())

    def move_right(self):
        self.goto(x=self.xcor() + MOVE_DISTANCE, y=self.ycor())

    def return_home(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
