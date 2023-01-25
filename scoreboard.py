FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.pu()
        self.ht()
        self.goto(-210, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level = {self.level}", align =  "center", font= FONT)
        self.level +=1
        
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over", align =  "center", font= FONT)
        
        
