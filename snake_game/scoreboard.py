from turtle import *
ALIGNMENT = "center"
FONT = ("Arial",15,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,220)
        self.text(f"Score: {self.score}")

    def text(self,text):
        self.write(text,move=False,align=ALIGNMENT,font= FONT)

    def update(self):
        self.score = self.score + 1
        self.clear()
        self.text(f"Score: {self.score}")

    def game_over(self):
        self.goto(0,0)
        self.text("Game Over")
