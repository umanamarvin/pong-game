from turtle import Turtle, Screen


class Paddle:

    def __init__(self):
        self.paddle = Turtle()
        self.create_paddle()

    def create_paddle(self):
        self.paddle.color('white')
        self.paddle.shape('square')
        self.paddle.penup()
        self.paddle.setheading(90)
        self.paddle.shapesize(stretch_len=4, stretch_wid=0.5)

    def move_paddle(self, position):
        self.paddle.goto(position)

    def control_paddle(self, screen, controls):

        def go_up():
            print(self.paddle.ycor())
            if self.paddle.ycor() <= 140:
                print('UP')
                self.paddle.forward(20)

        def go_down():
            print(self.paddle.ycor())
            if self.paddle.ycor() >= -140:

                print('DOWN')
                self.paddle.backward(20)

        screen.listen()
        screen.onkey(key=controls[0], fun=go_up)
        screen.onkey(key=controls[1], fun=go_down)


