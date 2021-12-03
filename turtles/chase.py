from typing import List
from turtle import Turtle, Screen, mainloop, register_shape, shape, ontimer
import threading
from threading import Timer, Thread
import random
from queue import Queue
# import alphabet
from turtles.utils import new_turtle
from turtles.threads import TurtleThread

__all__ = ['turtle_chase']


# ideas
# - turtle army march
# - crazy shit, like turtles chasing each other while changing color and speeding up and slowing down randomly
# - Roomba: turtle moves in clean orderly lines up and down
# - turtle writes out a message

# set turtle shapes
# register_shape('turtle.gif')
# shape('turtle.gif')

# multi threading example:
# https://stackoverflow.com/a/44833522


class TurtleChase:
    def __init__(self):
        self.fleet: List[Turtle] = []
        self.screen = Screen()
        self.colors = ['red', 'green', 'blue', 'magenta','yellow', 'cyan']
        self.turtle_index = -1
        num_cores = 4
        self.command_queue = Queue(num_cores - 1)

    def run(self):
        self.screen.bgcolor('black')
        self.screen.onclick(self.on_click, btn=2)
        # self.set_on_mouse_move_handler(self.on_mouse_move)
        self.process_queue()
        mainloop()

    def process_queue(self):
        while not self.command_queue.empty():
            handler, args, kwargs = self.command_queue.get()()
            handler(*args, **kwargs)

        ontimer(self.process_queue, 100)

    def push_command(self, handler, *args, **kwargs):
        self.command_queue.put((handler, args, kwargs))

    def on_click(self, x, y):
        # bump the turtle index
        self.turtle_index += 1

        # initialize the turtle
        turtle = new_turtle(x, y)

        # set color
        color_index = self.turtle_index % len(self.colors)
        color = self.colors[color_index]
        turtle.fillcolor(color)
        turtle.pencolor(color)
        # set size
        turtle.pensize('3')

        TurtleThread(turtle).start()
        # self.fleet.append(turtle)

    # causes program to crash
    def on_mouse_move(self, x, y):
        for turtle in self.fleet:
            angle = turtle.towards(x, y)
            print(f'{angle=}')
            turtle.left(angle)

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
