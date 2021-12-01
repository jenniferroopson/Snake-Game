from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.scoreboard()
        self.hideturtle()

    def scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Poppins", 18, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GameOver", align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()
