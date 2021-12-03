from typing import List
from turtle import Turtle, Screen, mainloop, register_shape, shape, ontimer
import threading
from threading import Timer, Thread
import random
from queue import Queue
from turtles.utils import new_turtle
from turtles import alphabet

__all__ = ['turtle_chase']


# ideas
# - turtle army march
# - crazy shit, like turtles chasing each other while changing color and speeding up and slowing down randomly
# - Roomba: turtle moves in clean orderly lines up and down
# - turtle writes out a message

# TODO:
# - finish character set, with all 26 capital letters, and !, ?
# - Make turtle start and stop on timer while drawing straight lines, so that he matches his ellipse speed



class TurtleChase:
    def __init__(self):
        self.screen = Screen()
        self.turtle = None
        self.screen.bgcolor('black')
        self.screen.onclick(self.on_click, btn=2)
        # self.set_on_mouse_move_handler(self.on_mouse_move)
        mainloop()

    def run(self):
        alphabet.write(self.turtle, 'GET OUT!')
        self.turtle = None

    def on_click(self, _x, _y):
        if self.turtle:
            print('I am very small, so you can imagine the kind of stress that I am under')
            return
        x, y = (0, 0)
        self.turtle = new_turtle(x=x, y=y, color='green', size=3, teleport=False, speed='slowest')
        self.run()

    def on_mouse_move(self, x, y):
        if not self.turtle:
            return
        turtle = self.turtle
        angle = turtle.towards(x, y)
        print(f'{angle=}')
        turtle.left(angle)

    # causes program to crash if to many commands are issued at once
    # https://stackoverflow.com/a/44214001
    def set_on_mouse_move_handler(self, handler):
        screen = self.screen

        def event_handler(event):
            handler(screen.cv.canvasx(event.x), -screen.cv.canvasy(event.y))

        if handler is None:
            screen.cv.unbind('<Motion>')
        else:
            screen.cv.bind('<Motion>', event_handler)


turtle_chase = TurtleChase()
