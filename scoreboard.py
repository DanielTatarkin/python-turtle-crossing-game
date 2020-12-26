from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:

    def __init__(self):
        self.level = 1
        self.leveltext = Turtle(visible=False)
        self.leveltext.penup()
        self.leveltext.setpos(-280, 260)
        self.leveltext.write(f"Level: {self.level}", font=FONT)

    def next(self):
        self.leveltext.clear()
        self.leveltext.setpos(-280, 260)
        self.level += 1
        self.leveltext.write(f"Level: {self.level}", font=FONT)

    def lose(self):
        self.losetext = Turtle(visible=False)
        self.losetext.penup()
        self.losetext.setpos(0, 0)
        self.losetext.write(f"GAME OVER!", align="center", font=FONT)
