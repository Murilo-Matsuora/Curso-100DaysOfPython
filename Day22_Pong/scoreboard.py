from turtle import Turtle
FONT = ("Imagine Font", 70, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.pu()
        self.color("white")
        self.l_points = 0
        self.r_points = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 210)
        self.write(arg=f"{self.l_points}", align="center", font=FONT)
        self.goto(50, 210)
        self.write(arg=f"{self.r_points}", align="center", font=FONT)
