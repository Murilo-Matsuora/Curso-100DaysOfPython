from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.pu()
        self.color("green")
        self.seth(90)

        self.reset_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reached_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.reset_position()
            return True
        return False

    def reset_position(self):
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])
