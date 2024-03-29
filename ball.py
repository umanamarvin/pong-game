from turtle import Turtle
from paddle import Paddle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        # self.ball = Turtle()
        self.create_ball()
        self.step_x = -10
        self.step_y = 10

    def create_ball(self):
        self.shape('circle')
        self.penup()
        self.color('green')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def move_ball_to_player(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto((new_x, new_y))

    def ball_bounce_border(self):
        if self.ycor() > 180 or self.ycor() < -180:
            # print('hey aquiiii')
            self.step_y *= -1

    def ball_bounce_paddle(self):
            self.step_x *= -1

    def ball_out_left(self):
        if self.xcor() < -280:
            print('Ball out left')
            self.goto(0,0)

    def ball_out_right(self):
        if self.xcor() > 280:
            print('Ball out right')
            self.goto(0,0)

