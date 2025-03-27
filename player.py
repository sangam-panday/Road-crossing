from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
    
    def Go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)
    def Go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(0, new_y)

    def is_level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    
    def start(self):
        self.goto(STARTING_POSITION)
            

    

