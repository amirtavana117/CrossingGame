from turtle import Turtle
STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def Up(self):
        self.forward(MOVE_DISTANCE)

    def win(self, y):
        if y >= FINISH_LINE:
            self.goto(STARTING_POSITION)
            return True
        return False
