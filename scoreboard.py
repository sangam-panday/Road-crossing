from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)

    def update_score_board(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font= FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font= FONT)
