import time
from turtle import Screen
from player import Player


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)


player = Player()
screen.listen()
screen.onkey(player.Up, "Up")

Game_is_on = True

while Game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
