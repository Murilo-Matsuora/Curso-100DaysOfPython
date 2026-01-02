from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ('ComicSans', 15, 'normal')
GAME_OVER_FONT = ('ComicSans', 25, 'normal')
HIGHSCORE_FILE_PATH = "./highscore.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0, 265)
        self.color("white")

        self.score = 0

        try:
            file = open(HIGHSCORE_FILE_PATH, "r")
        except FileNotFoundError as error:
            print(f"Creating highscore.txt... {error}")
            with open(HIGHSCORE_FILE_PATH, "w+") as file:
                file.write("0")
            file = open(HIGHSCORE_FILE_PATH, "r")

        try:
            self.highscore = int(file.read())
        except ValueError as error:
            self.highscore = 0

        file.close()

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  |  High Score: {self.highscore}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 15)
    #     self.clear()
    #     self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
    #     self.goto(0, -10)
    #     self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(HIGHSCORE_FILE_PATH, "w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.update_score()
