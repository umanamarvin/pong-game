from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score_1 = 0
        self.score_2 = 0
        pass

    def update_scoreboard(self):
        self.clear()
        self.color('white')
        self.goto(0, 160)
        self.write(arg='Score', align='center', font=("Arial", 24, "normal"))
        self.color('green')
        self.goto(-100, 160)
        self.write(arg=self.score_1, align='center', font=("Arial", 18, "normal"))
        self.color('green')
        self.goto(100, 160)
        self.write(arg=self.score_2, align='center', font=("Arial", 18, "normal"))

    def increase_player_1(self):
        self.score_1 += 1
        print(self.score_1)
        self.update_scoreboard()

    def increase_player_2(self):
        self.score_2 += 1
        print(self.score_2)
        self.update_scoreboard()

    def winner(self):
        if self.score_1 == 5:
            self.goto(0, 0)
            self.write(arg='The winner is player 1', align='center', font=("Arial", 24, "normal"))
            return False
        elif self.score_2 == 5:
            self.goto(0, 0)
            self.write(arg='The winner is player 2', align='center', font=("Arial", 24, "normal"))
            return False
        else:
            return True
