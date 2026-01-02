from turtle import Turtle

class Paddle:
    def __init__(self, spawn_coords):
        self.paddle = Turtle("square")
        self.paddle.pu()
        self.paddle.teleport(spawn_coords[0], spawn_coords[1])
        self.paddle.setheading(90)
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.color("white")

    def move_up(self):
        if self.paddle.ycor() + 20 < 232:
            self.paddle.forward(20)
        else:
            self.paddle.goto(self.paddle.xcor(), 238)

    def move_down(self):
        if self.paddle.ycor() - 20 > - 226:
            self.paddle.backward(20)
        else:
            self.paddle.goto(self.paddle.xcor(), - 230)