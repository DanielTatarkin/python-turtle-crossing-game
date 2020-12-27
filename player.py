from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 270


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reposition()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def check_win(self):
        return self.ycor() > FINISH_LINE_Y

    def reposition(self):
        self.reset()
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
