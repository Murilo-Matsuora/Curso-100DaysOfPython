from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWN_RANGE = (-220, 230)


class CarManager:
    def __init__(self):
        self.cars = []

    def generate_car(self):
        car = Turtle("square")
        car.pu()
        car.seth(180)
        car. shapesize(stretch_len=2)
        car.color(random.choice(COLORS))
        car.setpos(340, random.randint(SPAWN_RANGE[0], SPAWN_RANGE[1]))
        self.cars.append(car)

    def move_cars(self, level):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT)
            if car.xcor() <= -340:
                self.cars.remove(car)
                car.reset()
                car.hideturtle()

    def detect_collision(self, player):
        for car in self.cars:
            if abs(car.xcor() - player.xcor()) <= 30 and abs(car.ycor() - player.ycor()) <= 15:
                return True
        return False
