from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.color('white')
        self.shape('square')
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=4, stretch_wid=0.5)

    def move_paddle(self, position):
        self.goto(position)

    def control_paddle(self, screen, controls):

        def go_up():
            if self.ycor() <= 140:
                print('UP')
                self.forward(20)

        def go_down():
            if self.ycor() >= -140:
                print('DOWN')
                self.backward(20)

        screen.listen()
        screen.onkey(key=controls[0], fun=go_up)
        screen.onkey(key=controls[1], fun=go_down)
