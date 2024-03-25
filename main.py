from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import Screen
import constants, time

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

player_1 = Paddle()
player_1.move_paddle(constants.POSITION_PLAYER_1)

player_2 = Paddle()
player_2.move_paddle(constants.POSITION_PLAYER_2)

ball = Ball()

game_on = True

while game_on:
    player_1.control_paddle(screen=screen, controls=constants.CONTROLS_PLAYER_1)
    player_2.control_paddle(screen= screen, controls=constants.CONTROLS_PLAYER_2)

    ball.move_ball_to_player_2()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()