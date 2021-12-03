from turtle import Turtle
from turtles.utils import copy_turtle


def A(turtle):
    turtle.left(60)
    turtle.forward(50)
    copy = copy_turtle(turtle)
    copy.right(60)
    copy.forward(45)
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(100)
