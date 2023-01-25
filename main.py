import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


scoreboard = Scoreboard()
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
            scoreboard.game_over()
            
    if tim.ycor() > 280:
        tim.reset()
        carmanager.level_up()
        scoreboard.update_scoreboard()
        
    
screen.exitonclick()