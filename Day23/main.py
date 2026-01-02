import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_over = False
while not game_over:
    time.sleep(0.05)
    screen.update()

    if player.reached_finish_line():
        scoreboard.increase_score()

    if random.randint(0, 5) == 0:
        car_manager.generate_car()

    car_manager.move_cars(scoreboard.level)

    if car_manager.detect_collision(player):
        scoreboard.print_game_over()
        game_over = True

screen.update()
screen.exitonclick()
