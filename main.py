from turtle import *
from random import *

colors = ["green", "red", "purple", "brown", "blue", "pink", "orange"]


def draw_shapes(tim , degree, i):
    tim.pencolor(choice(colors))
    tim.pensize(3)
    for j in range(0, i):
        tim.forward(90)
        tim.right(degree)


tim = Turtle()
tim.shape("triangle")
tim.penup()
tim.setx(-50)
tim.sety(300)
tim.pendown()
for i in range(3, 8):
    draw_shapes(tim, 360/i, i)


my_screen = Screen()
my_screen.exitonclick()