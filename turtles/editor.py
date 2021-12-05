import random

from typing import Iterable
from turtle import Turtle

from turtles.utils import retreat, walk, add, vector
from turtles.types import Path
from turtles.charset import character_set


def publish(turtle: Turtle, lines: Iterable[str], scramble: bool = False) -> None:
    # character width
    width = 50
    # space between characters
    margin = 25
    height = 100
    characters = character_set(width=float(width), height=float(height))
    shift_x = width + margin
    shift_y = height + margin
    (x, y) = (-700, 300)

    paths = [
        path.shift(vector(x + i * shift_x, y - j * shift_y))
        for (j, phrase) in enumerate(lines)
        for (i, c) in enumerate(phrase)
        for path in characters[c]
    ]

    if scramble:
        random.shuffle(paths)
        turtle.speed(9)

    for path in paths:
        path.draw(turtle)

    retreat(turtle)
