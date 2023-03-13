import colorgram
import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
turtle.colormode(255)
ch = colorgram.extract('image.jpg', 10)
lista = []
tim.penup()
tim.speed("fastest")
tim.hideturtle()
x = -250
y = -250
tim.setx(x)
tim.sety(y)
for i in ch:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    tup = (r, g, b)
    lista.append(tup)

for i in range(10):
    for o in range(10):
        tim.pendown()
        tim.dot(20, random.choice(lista))
        tim.penup()
        tim.forward(50)
    y += 50
    tim.setx(x)
    tim.sety(y)

screen = Screen()
screen.exitonclick()
