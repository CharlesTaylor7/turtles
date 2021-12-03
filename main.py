from typing import List
from turtle import Turtle, Screen, mainloop, register_shape, shape, ontimer
from threading import Timer
import random

# ideas
# - turtle army march
# - crazy shit, like turtles chasing each other while changing color and speeding up and slowing down randomly
# - Roomba: turtle moves in clean orderly lines up and down
# - turtle writes out a message

# set turtle shapes
# register_shape('turtle.gif')
# shape('turtle.gif')

class TurtleChase:
    def __init__(self):
        self.fleet: List[Turtle] = []
        self.screen = Screen()
        self.colors = ['red', 'green', 'blue', 'magenta','yellow', 'cyan']
        self.turtle_index = -1

    def run(self):
        self.screen.bgcolor('black')
        self.screen.onclick(self.on_click, btn=2)
        # self.set_on_mouse_move_handler(self.on_mouse_move)
        mainloop()

    def on_click(self, x, y):
        # bump the turtle index
        self.turtle_index += 1

        # initialize the turtle
        turtle = Turtle()
        turtle.setundobuffer(None)
        place(turtle, x, y)
        turtle.speed('slowest')

        # set color
        color_index = self.turtle_index % len(self.colors)
        color = self.colors[color_index]
        turtle.fillcolor(color)
        turtle.pencolor(color)
        # set size
        turtle.pensize('3')

        # allow himb to be dragged
        turtle.onclick(lambda *args: turtle.penup())
        turtle.ondrag(turtle.goto)
        turtle.onrelease(lambda *args: turtle.pendown())

        turtle.circle(30)
        spin(turtle)
        nudge(turtle)
        self.fleet.append(turtle)

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


def spin(turtle):
    turtle.left(random.randint(1, 360))


def nudge(turtle):
    def move():
        turtle.forward(10)
        ontimer(move, 400)

    move()


def place(turtle, x, y):
    current_speed = turtle.speed()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.speed(current_speed)


TurtleChase().run()
