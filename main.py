from typing import List
from turtle import Turtle, Screen, mainloop, register_shape, shape, ontimer
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
        self.screen = Screen()
        self.throttle = False

    def run(self):
        self.screen.onclick(self.on_click)
        self.set_on_mouse_move_handler(self.on_mouse_move)
        mainloop()

    def on_click(self, x, y):
        turtle = Turtle()
        turtle.speed('slowest')
        place(turtle, x, y)
        nudge(turtle)
        self.fleet.append(turtle)

    def on_mouse_move(self, x, y):
        for turtle in self.fleet:
            turtle.left(turtle.towards(x, y))

    def reset_throttle(self):
        self.throttle = False

    # https://stackoverflow.com/a/44214001
    def set_on_mouse_move_handler(self, handler):
        screen = self.screen

        def event_handler(event):
            if self.throttle:
                return
            handler(screen.cv.canvasx(event.x), -screen.cv.canvasy(event.y))
            self.throttle = True

            ontimer(self.reset_throttle, 400)

        if handler is None:
            screen.cv.unbind('<Motion>')
        else:
            screen.cv.bind('<Motion>', event_handler)


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
