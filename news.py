from turtles.alphabet import write as old_write
from turtles.new_alphabet import write as new_write
from turtles.utils import new_turtle

from turtle import mainloop, Screen


screen = Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
t = new_turtle(speed=0, pen_size=3)

new_write(t, 'the quick brown fox!'.upper().split())
mainloop()
