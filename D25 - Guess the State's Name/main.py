import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. Name the States Game")
background_image = "blank_states_img.gif"
screen.addshape(background_image)
turtle.shape(background_image)
data = pandas.read_csv("50_states.csv")
lower_states = data.state.str.lower()
c_a = []
while len(c_a) < 50:
    answer_state = screen.textinput(title=f"{len(c_a)}/50 States Correct", prompt="What's another state in the U.S.?")
    if answer_state.lower() == "exit":
        estados_no_sabidos = []
        estados_en_lista = data.state.to_list()
        for i in estados_en_lista:
            if i not in c_a:
                estados_no_sabidos.append(i)
        print(c_a)
        print(estados_no_sabidos)

        break
    for i in lower_states:
        if i == answer_state.lower():
            text = turtle.Turtle()
            text.hideturtle()
            text.color("black")
            text.penup()
            text.goto(int(data[lower_states == i].x), int(data[lower_states == i].y))
            text.write(f"{i.title()}", move=False, align="center", font=('Arial', 15, 'bold'))
            c_a.append(answer_state.title())
new_file = pandas.DataFrame(estados_no_sabidos)
new_file.to_csv("states_to_learn.csv")
