from typing import List
from turtle import Turtle, Screen, mainloop, register_shape, shape, ontimer
from threading import Timer
import random

# ideas
# - on every click the turtle turns at random and moves 100 steps forward
# - turtle chases the mouse in real time
# - fleet of turtles
# - crazy shit, like turtles chasing each other while changing color and speeding up and slowing down randomly
# - Roomba: turtle moves in clean orderly lines up and down
# - every click spawns a new turtle

# set turtle shapes
# register_shape('turtle.gif')
# shape('turtle.gif')

class TurtleChase:
    def __init__(self):
        self.fleet: List[Turtle] = []
        self.new_turtle = None
        self.screen = Screen()

    def run(self):
        self.screen.onclick(self.on_click)
        # self.screen.ondrag(self.new_turtle.goto)
        # self.screen.onrelease(self.on_release)
        self.set_on_mouse_move_handler(self.on_mouse_move)
        mainloop()

    def on_click(self, x, y):
        self.new_turtle = Turtle()
        self.new_turtle.setundobuffer(None)
        print(self.new_turtle.undobuffer)
        place(self.new_turtle, x, y)
        self.new_turtle.speed('slowest')
        self.new_turtle.penup()
        # allow himb to be dragged
        self.new_turtle.ondrag(self.new_turtle.goto)

        # nudge(turtle)
        # self.fleet.append(turtle)

    def on_release(self, x, y):
        self.fleet.append(self.new_turtle)
        self.new_turtle = None

    def on_mouse_move(self, x, y):
        # print(x, y)
        return
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


def nudge(turtle):
    def move():
        turtle.forward(10)
        ontimer(move, 400, add=True)

    move()


def place(turtle, x, y):
    current_speed = turtle.speed()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.speed(current_speed)


TurtleChase().run()
