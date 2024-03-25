from turtle import Turtle
from paddle import Paddle


class Ball(Paddle):

    def __init__(self):
        self.ball = Turtle()
        self.create_ball()

    def create_ball(self):
        self.ball.shape('circle')
        self.ball.penup()
        self.ball.color('green')
        self.ball.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def move_ball_to_player_1(self):
        self.ball.setheading(180)
        self.ball.forward(10)

    def move_ball_to_player_2(self):
        self.ball.setheading(0)
        self.ball.forward(10)

    def ball_impact(self):
        pass

    def ball_physics(self):
        pass

