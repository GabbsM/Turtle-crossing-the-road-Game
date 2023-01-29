
from turtle import Screen
from my_turtle import My_Turtle
from score import Score


screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor('white')


turtle = My_Turtle()
score = Score()

screen.listen()
screen.onkey(turtle.go_up, 'Up')
screen.onkey(turtle.go_down, 'Down')



on_game = True
while on_game:
    screen.update()

    if turtle.ycor() > 230:
        turtle.left(180)
        score.point()
        turtle.goto(0, 225)
    elif turtle.ycor() < -260:
        turtle.right(180)
        score.point()
        turtle.goto(0, -250)






screen.exitonclick()