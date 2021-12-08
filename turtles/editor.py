import random

from typing import Iterable, Tuple
from turtle import Turtle, Screen

from turtles.utils import retreat, vector
from turtles.charset import character_set


def get_canvas_size() -> Tuple[float, float]:
    root_tk = Screen()._root  # type: ignore
    return (root_tk.win_width(), root_tk.win_height())  # type: ignore


def publish(turtle: Turtle, lines: Iterable[str], scramble: bool = False) -> None:
    (canvas_width, canvas_height) = get_canvas_size()

    # character dimensions
    width = 40
    height = 60
    # space between characters
    margin = width / 2
    characters = character_set(width=float(width), height=float(height))
    shift_x = width + margin
    shift_y = height + margin
    (x, y) = (-canvas_width/2 + margin, canvas_height/2 - 2*height)

    paths = [
        path.shift(vector(x + i * shift_x, y - j * shift_y))
        for (j, phrase) in enumerate(lines)
        for (i, c) in enumerate(phrase.upper())
        for path in characters[c]
    ]

    if scramble:
        random.shuffle(paths)
        turtle.speed(9)

    for path in paths:
        path.draw(turtle)

    retreat(turtle)
