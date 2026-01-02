from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.pu()
        self.goto(-200, 240)
        self.level = 0
        self.update_scoreboard()

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def print_game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!\n You got to level: {self.level}", align="center", font=FONT)
