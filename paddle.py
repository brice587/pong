from turtle import Turtle

LENGTH = 1
WIDTH = 5
MOVE = 20


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_len=LENGTH, stretch_wid=WIDTH)
        self.color("white")
        self.goto(x=x, y=y)

    def go_up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(), new_y)
