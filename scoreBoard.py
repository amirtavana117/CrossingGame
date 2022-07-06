from turtle import Turtle


FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.update_scordboard()

    def update_scordboard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f"Score:{self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1

    def Game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
