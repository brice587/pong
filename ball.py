from turtle import Turtle

LENGTH = 1
WIDTH = 1
X = 0
Y = 0


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.turtlesize(stretch_len=LENGTH, stretch_wid=WIDTH)
        self.color("white")
        self.goto(x=X, y=Y)
        self.x_move = 10
        self.y_move = 8
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self, game_mode):
        self.x_move *= -1
        if game_mode == "hard":
            self.move_speed *= 0.9

    def reset(self):
        self.goto(x=X, y=Y)
        self.move_speed = 0.1
        self.bounce_x()
