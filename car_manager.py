from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 2


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.starting_move_distance = 5

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color("black", random.choice(COLORS))
            car.penup()
            car.seth(180)

            random_y = random.randint(-250, 250)
            car.goto(320, random_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.starting_move_distance)

    def increase_speed(self):
        self.starting_move_distance += MOVE_INCREMENT
