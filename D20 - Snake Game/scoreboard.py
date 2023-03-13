from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.counter} High Score: {self.high_score}", move=False, align="center", font=('Arial', 20, 'bold'))

    def increase_score(self):
        self.counter += 1
        self.update_scoreboard()

    def reset(self):
        if self.counter > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.counter))
        self.counter = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align="center", font=('Arial', 20, 'bold'))
