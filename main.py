import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



carmanager = CarManager()
tim = Player()
screen.listen()
screen.onkey(tim.up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_Car()
    carmanager.move_cars()
    
    for car in carmanager.all_cars:
        if car.distance(tim) <=20:
            game_is_on = False
    
    
    tim.reset()


screen.exitonclick()