from turtle import exitonclick
from turtles.utils import new_turtle, DancingTurtle, new_screen

s = new_screen(title='rave', bgcolor='black')

t = new_turtle(DancingTurtle, color='cyan', turtle_size=10, speed=9)
t.dance()

exitonclick()
