from turtle import exitonclick, Screen
from turtles.utils import new_turtle, DancingTurtle

s = Screen()
s.bgcolor('black')

t = new_turtle(DancingTurtle, color='cyan', turtle_size=10, speed=9)
t.dance()

exitonclick()
