from turtle import exitonclick, Screen
from turtles.utils import new_turtle, dance

s = Screen()
s.bgcolor('black')

t = new_turtle(color='cyan', turtle_size=10, speed=9)
dance(t)

exitonclick()
