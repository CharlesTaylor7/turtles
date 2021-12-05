import random

from typing import List, Callable, cast, Optional, Iterable, NoReturn
from turtle import Turtle, Screen, mainloop, register_shape, shape, ontimer, textinput
from queue import Queue
from adt import adt
from tkinter import Event, Canvas

from turtles.utils import new_turtle
from turtles import alphabet


class MouseEvent:
    x: float
    y: float


class TurtleNews:
    def __init__(self) -> None:
        self.turtle: Optional[Turtle] = None
        self.busy = False
        self.screen = Screen()
        self.screen.bgcolor('black')

    def start(self) -> NoReturn:  # type: ignore[misc]
        self.screen.onclick(self.on_click, btn=2)
        # self.set_on_mouse_move_handler(self.on_mouse_move)
        mainloop()

    def on_click(self, _x: float, _y: float) -> None:
        if self.busy:
            print('I am very small, so you can imagine the kind of stress that I am under')
            return

        # ask for input
        phrase: Optional[str] = textinput('???', '?')

        if phrase:
            self.publish(phrase.split('\n'))

    def publish(self, article: Iterable[str]) -> None:
        # mark busy
        self.busy = True

        # summon a turtle
        self.turtle = new_turtle(pen_size=3)

        # write the phrase
        alphabet.write(self.turtle, article)

        # mark available
        self.busy = False

    def on_mouse_move(self, x: float, y: float) -> None:
        if not self.turtle:
            return
        turtle = self.turtle
        angle = turtle.towards(x, y)
        turtle.left(angle)

    # causes program to crash if to many commands are issued at once
    # https://stackoverflow.com/a/44214001
    def set_on_mouse_move_handler(self, handler: Callable[[float, float], None]) -> None:
        screen = self.screen

        def event_handler(event: Event[Canvas]) -> None:
            handler(screen.cv.canvasx(event.x), -screen.cv.canvasy(event.y))

        if handler is None:
            screen.cv.unbind('<Motion>')
        else:
            screen.cv.bind('<Motion>', event_handler)
