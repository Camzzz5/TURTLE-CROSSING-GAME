import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



cars = []
tim = Player()
traffic = CarManager()
screen.listen()
screen.onkey(tim.up,"Up")

j = 0
game_is_on = True
while game_is_on:
    j+=1
    time.sleep(0.1)
    screen.update()
    if j == 6:
        car = CarManager()
        cars.append(car)
        j = 0
    for c in cars:
        c.movement()
    # tim.turtle_movement()
    tim.reset()


screen.exitonclick()