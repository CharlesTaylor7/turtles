import math
from typing import List, Tuple, Callable, Optional, Dict, Union, Iterable, cast, Generic
from turtle import Turtle, Vec2D
from dataclasses import dataclass, field
from typeguard import typechecked
from adt import adt, Case
from fractions import Fraction

from turtles.utils import retreat, walk, to_radians, line, vector, line_to, add, new_turtle
from turtles.config import settings
from turtles.types import Point
from turtles.alphabet import character_set, Stroke





def rewrite() -> None:
    turtle = new_turtle(speed=0)
    # character width
    width = 50
    # space between characters
    margin = 25
    height = 100
    characters = character_set(width=float(width), height=float(height))
    new: Dict[str, List[str]] = dict()
    for c, strokes in characters.items():
        new[c] = list()
        # reset turtle  position 
        walk(turtle, (0, 0))

        # turtles initial position for this character
        turtle.char_position = vector(0, 0)  # type: ignore

        def apply_stroke(s: Stroke) -> None:
            start = turtle.position()
            if s.offset:
                walk(turtle, s.offset)

            if s.heading is not None:
                turtle.setheading(s.heading)

            s.path(turtle, **s.kwargs)
            end = turtle.position()
            new[c].append(Path(start=start, end=end).rescale(width=width, height=height))

        for s in strokes:
            apply_stroke(s)

    with open('new_char_set.py', 'a') as file:
        file.write(str(new))


def rescale(point: Point, width: float, height: float) -> str:
    x = rescale_1d(point[0], width, 'w')
    y = rescale_1d(point[1], height, 'h')
    return f'({x}, {y})'


def rescale_1d(x: float, s: float, char: str) -> str:
    if x == 0:
        return '0'
    d = s / x
    sign = '-' if d < 0 else ''
    d = abs(d)

    if d > 8.001:
        return '0'

    d, n = Fraction(d).limit_denominator(8).as_integer_ratio()
    n_s = f'{n}*' if n != 1 else ''
    d_s = f'/{d}' if d != 1 else ''
    return f'{sign}{n_s}{char}{d_s}'



@dataclass
class Path:
    start: Point
    end: Point

    def rescale(self, width: float, height: float) -> str:
        return f'Path(start={rescale(self.start, width, height)}, end={rescale(self.end, width, height)})'
