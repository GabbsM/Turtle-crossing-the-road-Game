from turtle import Turtle


class My_Turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.left(90)
        self.shape('turtle')
        self.penup()
        self.goto(0, -250)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



