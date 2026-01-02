from turtle import Turtle

class Background(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.draw_divisor()
        self.draw_horizontal_line((- 410, 293))
        self.draw_horizontal_line((- 410, -287))

    def draw_divisor(self):
        self.pu()
        self.goto(0, 290)
        self.pd()
        self.seth(270)

        while self.ycor() > -300:
            self.pu()
            self.draw_square(8)
            self.goto(0, self.ycor() - 8)
            self.pd()

    def draw_square(self, side_length):
        self.goto(self.xcor() - side_length/2, self.ycor())
        self.begin_fill()
        self.goto(self.xcor() + side_length, self.ycor())
        self.goto(self.xcor(), self.ycor() - side_length)
        self.goto(self.xcor() - side_length, self.ycor())
        self. end_fill()

    def draw_horizontal_line(self, coords):
        self.pu()
        self.goto(coords[0], coords[1])
        self.pd()
        self.seth(0)
        self.pensize(width=10)
        self.forward(820)

    def print_win_message(self, message):
        self.pu()
        self.goto(0, 30)
        self.write(arg="GAME OVER", align="center", font=("Imagine Font", 50, "bold"))
        self.goto(0, 0)
        self.write(arg=message, align="center", font=("Imagine Font", 30, "bold"))

    def reset_background(self):
        self.clear()
        self.draw_horizontal_line((- 410, 293))
        self.draw_horizontal_line((- 410, -287))
