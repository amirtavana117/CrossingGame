from turtle import Turtle
import random

COLORS = ["Red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITON = [-100, -80, -60, -40, -20, 0, 10, 30, 60, 90, 110, 120, 150]
STARTING_MOVE_DISTANCE = 5

MOVE_FORWARD = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.Cars = []
        self.hideturtle()
        self.Create_car()

    def Create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=random.randint(1, 7),
                          stretch_wid=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.Cars.append(new_car)
    
