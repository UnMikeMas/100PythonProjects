from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        if self.ycor() > 250:
            pass
        else:
            self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        if self.ycor() < -230:
            pass
        else:
            self.goto(self.xcor(), self.ycor()-20)

