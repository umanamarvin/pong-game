from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import Screen
import constants
import time

# Create the screen
screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Create the two players
player_1 = Paddle()
player_1.move_paddle(constants.POSITION_PLAYER_1)
player_2 = Paddle()
player_2.move_paddle(constants.POSITION_PLAYER_2)

# Create the ball and scoreboard objects
ball = Ball()
scoreboard = Scoreboard()

# Game loop until game_status is False
game_status = True
while game_status:

    scoreboard.update_scoreboard()

    player_1.control_paddle(screen=screen, controls=constants.CONTROLS_PLAYER_1)
    player_2.control_paddle(screen=screen, controls=constants.CONTROLS_PLAYER_2)

    ball.move_ball_to_player()
    ball.ball_bounce_border()

    if ball.distance(player_1) < 50 and ball.xcor() < -270:
        ball.ball_bounce_paddle()

    if ball.distance(player_2) < 50 and ball.xcor() > 270:
        ball.ball_bounce_paddle()

    if ball.ball_out_left():
        scoreboard.increase_player_2()
    elif ball.ball_out_right():
        scoreboard.increase_player_1()

    screen.update()
    time.sleep(0.05)

    game_status = scoreboard.winner()

screen.exitonclick()
