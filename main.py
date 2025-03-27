import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Chicken Cross Road")
screen.tracer(0)

p= Player()
c= CarManager()
s = Scoreboard()

screen.listen()
screen.onkey(p.Go_up, "Up")
screen.onkey(p.Go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    c.create_car()
    c.move_cars()
    s.update_score_board()


    for car in c.all_cars:
        if car.distance(p) < 20:
            game_is_on = False
            s.game_over()

    if p.is_level_up():
        p.start()
        s.increase_level()

screen.exitonclick()