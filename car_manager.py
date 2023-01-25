COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.new_x = -290
        self.cars = []
        self.shape("square")
        self.setheading(0)
        self.shapesize(stretch_len=2, stretch_wid = 1)
        self.pu()
        self.color(random.choice(COLORS))
        self.new_y = random.randint(-300, 300)
        self.goto(self.new_x, self.new_y)
        
    
    
    def movement(self):
        self.fd(STARTING_MOVE_DISTANCE)
        
        # self.fd(STARTING_MOVE_DISTANCE)
        
        
        
    
