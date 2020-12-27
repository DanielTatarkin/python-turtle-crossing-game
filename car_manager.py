from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 0.3
MOVE_INCREMENT = 0.1


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        if random.randint(0, 200) > 1:
            return
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.setpos(300, float(random.randint(-220, 220)))
        self.cars.append(car)

    def move_cars(self, player):
        for car in self.cars:
            car.forward(self.speed)

            if player.distance(car) < 20:
                return False
            if car.xcor() <= -350:
                car.hideturtle()
                self.cars.remove(car)
        return True

    def speedup(self):
        self.speed += MOVE_INCREMENT
