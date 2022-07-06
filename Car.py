from turtle import Turtle
import random

COLORS = ["Red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

MOVE_FORWARD = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.Cars = []
        self.hideturtle()
        self.carSpeed = MOVE_FORWARD

    def Create_car(self):
        random_chance_to_create_car = random.randint(1, 7)
        if random_chance_to_create_car == 6:
            new_car = Turtle("square")

            new_car.shapesize(stretch_len=random.randint(1, 7),
                              stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.Cars.append(new_car)
        else:
            pass

    def Move(self):
        for car in self.Cars:
            car.setheading(180)
            car.forward(self.carSpeed)

    def Increase_speed(self):
        self.carSpeed += MOVE_FORWARD
