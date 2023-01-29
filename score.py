import turtle
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.score = 0
        self.penup()

        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 265)
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def point(self):
        self.score += 1
        self.update_score()








