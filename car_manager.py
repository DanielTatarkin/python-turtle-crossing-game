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
        car = Turtle("rectangle")
        car.penup()
        car.setpos(300, float(random.randint(-220, 250)))
        car.left(180)
        car.color(random.choice(COLORS))
        self.cars.append(car)

    def move_cars(self, player):
        for car in self.cars:
            car.forward(self.speed)
            # x_distance = player.turtle.xcor() - car.xcor()
            # y_distance = player.turtle.ycor() - car.ycor()
            # print(f"x_dist: {x_distance}     y_dist: {y_distance}")

            if player.turtle.distance(car) < 20:
                return False
            if car.xcor() <= -350:
                car.hideturtle()
                self.cars.remove(car)
        return True

    def speedup(self):
        self.speed += MOVE_INCREMENT


