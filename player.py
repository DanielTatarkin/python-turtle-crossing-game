from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 270


class Player:

    def __init__(self):
        self.turtle = Turtle("turtle")
        self.reset()

    def move(self):
        self.turtle.forward(MOVE_DISTANCE)

    def check_win(self):
        return self.turtle.ycor() > FINISH_LINE_Y

    def reset(self):
        self.turtle.reset()
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.goto(STARTING_POSITION)
