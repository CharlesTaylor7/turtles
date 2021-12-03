from typing import List
from turtle import Turtle, Screen, mainloop, register_shape, shape, ontimer
import threading
from threading import Timer, Thread
import random
from queue import Queue
from turtles.utils import new_turtle
from turtles import alphabet

__all__ = ['TurtleThread']


class TurtleThread(Thread):
    def __init__(self, turtle):
        super().__init__(daemon=True)
        self.turtle = turtle

    def run(self):
        alphabet.A(self.turtle)
        #self.A()
       # self.circle()


       # self.spin()
       # self.nudge()

