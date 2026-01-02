import math
from turtle import Turtle
import random

class Ball:
    def __init__(self):
        self.ball = Turtle("circle")
        self.ball.pu()
        self.ball.teleport(0, 0)
        self.ball.color("white")
        self.delta_x = random.random() * 1.5 + 1.5
        self.delta_y = math.sqrt(3 * 3 - self.delta_x * self.delta_x) * random.choice([1, -1])
        self.speed = 1
        self.set_random_direction()

    def move(self):
        new_x = self.ball.xcor() + self.delta_x * self.speed
        new_y = self.ball.ycor() + self.delta_y * self.speed
        self.ball.goto(new_x, new_y)

    def bounce(self):
        self.delta_y = -self.delta_y

    def hit(self):
        self.delta_x = -self.delta_x
        self.increase_speed()

    def reset_position(self, direction):
        self.ball.goto(0, 0)
        self.delta_x = abs(self.delta_x) * direction

    def reset_speed(self):
        self.speed = 1

    def set_random_direction(self):
        self.delta_x = random.random() * 1.5 + 1.5
        self.delta_y = math.sqrt(3 * 3 - self.delta_x * self.delta_x) * random.choice([1, -1])

    def increase_speed(self):
        if self.delta_x * self.delta_x + self.delta_y * self.delta_y < 10 * 10:
            self.speed += 0.5
