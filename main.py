from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
game_mode = screen.textinput(title="Game Mode", prompt="Choose 'Easy' or 'Hard' mode: ").lower()
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

score_board = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect ball colliding with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x(game_mode)

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset()
        score_board.left_score()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset()
        score_board.right_score()

    if score_board.r_score == 5 or score_board.l_score == 5:
        game_is_on = False

screen.exitonclick()
