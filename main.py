import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtler")
screen.bgpic("double_road.jpg")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    # Detecting collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 19:
            game_is_on = False
            scoreboard.game_over()

    # Starting next level
    if player.ycor() == 280:
        car_manager.increase_speed()
        player.next_level()
        scoreboard.level_up()

screen.exitonclick()
