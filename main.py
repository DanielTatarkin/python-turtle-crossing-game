import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main():
    player = Player()
    screen = setup_screen(player)
    scoreboard = Scoreboard()
    car_manager = CarManager()

    game_is_on = True
    while game_is_on:
        car_manager.spawn_car()
        screen.update()
        if not car_manager.move_cars(player):
            scoreboard.lose()
            game_is_on = False
            exit(0)
        if player.check_win():
            scoreboard.next()
            player.reposition()
            car_manager.speedup()


def setup_screen(player):
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.register_shape("rectangle", ((-10, -15), (-10, 15), (10, 15), (10, -15)))
    screen.listen()
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_up, "w")
    return screen


if __name__ == '__main__':
    main()
