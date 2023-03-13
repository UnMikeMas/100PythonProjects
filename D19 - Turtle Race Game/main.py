from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y = -120
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
if user_choice:
    is_race_on = True
for _ in colors:
    tim = Turtle(shape="turtle")
    tim.color(_)
    tim.penup()
    tim.goto(x=-210, y=y)
    y += 50
    all_turtles.append(tim)
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You won, the {winning_color} turtle won!")
            else:
                print(f"You lost, the {winning_color} turtle won :/")
            is_race_on = False
        turtle.forward(random.randint(0, 10))
screen.exitonclick()
