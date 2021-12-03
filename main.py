from typing import List
from turtle import Turtle, Screen, mainloop, register_shape, shape, ontimer
import threading
from threading import Timer, Thread
import random
from queue import Queue


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
            self.command_queue.get()()

        ontimer(self.process_queue, 100)

    def push_command(self, command):
        self.command_queue.put(command)

    def on_click(self, x, y):
        # bump the turtle index
        self.turtle_index += 1

        # initialize the turtle
        turtle = Turtle('turtle')
        turtle.setundobuffer(None)
        place(turtle, x, y)
        turtle.speed('fastest')

        # set color
        color_index = self.turtle_index % len(self.colors)
        color = self.colors[color_index]
        turtle.fillcolor(color)
        turtle.pencolor(color)
        # set size
        turtle.pensize('3')

        TurtleThread(turtle, self.command_queue.put).start()
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


def place(turtle, x, y):
    current_speed = turtle.speed()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.speed(current_speed)


class TurtleThread(Thread):
    def __init__(self, turtle, push_command):
        super().__init__(daemon=True)
        self.turtle = turtle
        self.push_command = push_command

    def run(self):
        self.circle()
        self.spin()
        self.nudge()

    def spin(self):
        self.push_command(lambda: self.turtle.left(random.randint(1, 360)))

    def nudge(self):
        def move():
            self.push_command(lambda: self.turtle.forward(10))
            ontimer(move, 400)
        move()

    def circle(self):
        for _ in range(360):
            self.push_command(lambda: self.turtle.forward(1))
            self.push_command(lambda: self.turtle.left(1))


TurtleChase().run()
