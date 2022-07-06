import time
from turtle import Screen
from player import Player
from Car import Car

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)


player = Player()
car = Car()
screen.listen()
screen.onkey(player.Up, "Up")

Game_is_on = True

while Game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
