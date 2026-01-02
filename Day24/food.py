from turtle import Turtle
import random
from snake import PIXEL_SIZE

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.85, stretch_wid=0.65, outline=2)
        self.color("red")
        self.pencolor("DarkRed")
        self.refresh()

    def refresh(self):
        random_x = random.randint(round(- 580 / (2 * PIXEL_SIZE)), round(580 / (2 * PIXEL_SIZE)))
        random_y = random.randint(round(- 580 / (2 * PIXEL_SIZE)), round(580 / (2 * PIXEL_SIZE)))
        self.goto(random_x * PIXEL_SIZE, random_y * PIXEL_SIZE)
