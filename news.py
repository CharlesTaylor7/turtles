from turtles.new_alphabet import write
from turtles.utils import new_turtle

from turtle import mainloop, Screen


screen = Screen()
screen.setup(width=1.0, height=1.0, startx=None, starty=None)

write(
    new_turtle(speed=0, pen_size=3),
    'the quick brown fox\n jumped over the lazy dog!'.upper().split("\n")
)

mainloop()
