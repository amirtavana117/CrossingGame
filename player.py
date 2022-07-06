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
        new_x = self.xcor + MOVE_DISTANCE
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def Down(self):
        self.backward(MOVE_DISTANCE)
