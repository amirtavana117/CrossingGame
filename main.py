import time
from turtle import Screen
from player import Player
from Car import Car
from scoreBoard import ScoreBoard
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)


player = Player()
car = Car()
scoreboard = ScoreBoard()   
screen.listen()
screen.onkey(player.Up, "Up")

Game_is_on = True

while Game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scordboard()
    car.Create_car()
    car.Move()
    for car_r in car.Cars:
        if car_r.distance(player) < 20:
            scoreboard.Game_over()
            Game_is_on = False
    if player.win(player.ycor()):
        car.Increase_speed()
        scoreboard.increase_score()


screen.exitonclick()
