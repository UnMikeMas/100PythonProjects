import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
angle = 5
turtle.colormode(255)
timmy_the_turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup


for i in range(int(round(360/angle))):
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(angle)
    timmy_the_turtle.color(random_color())

screen = Screen()
screen.exitonclick()
