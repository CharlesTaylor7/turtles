import random

from typing import Optional, Iterable 
from turtles.editor import publish
from turtles.utils import new_turtle, DancingTurtle, new_screen

from turtle import mainloop, Turtle, Screen, textinput

screen = new_screen('Tic Tac Toe')

wise_turtle = new_turtle(DancingTurtle)
mainloop()
