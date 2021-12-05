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




def write(turtle: Turtle, lines: Iterable[str]) -> None:
    # character width
    width = 50
    # space between characters
    margin = 25
    height = 100
    characters = character_set(width=float(width), height=float(height))
    shift_x = width + margin
    shift_y = height + margin
    (x, y) = (-700, 300)
    for (j, phrase) in enumerate(lines):
        for (i, c) in enumerate(phrase):
            print(f'drawing \'{c}\'')
            paths = characters.get(c)
            if paths is None:
                raise Exception(f'skipping undefined \'{c}\'')

            # walk to next character
            walk(turtle, (x + i * shift_x, y - j * shift_y))

            # turtles initial position for this character
            p: Vec2D = turtle.position()

            def apply_path(s: Path) -> None:
                start = add(p, s.start)
                end = add(p, s.end)
                walk(turtle, start)
                turtle.setheading(turtle.towards(end))
                turtle.goto(end)

            for s in paths:
                apply_path(s)

    retreat(turtle)


@dataclass
class Path:
    start: Point
    end: Point


def character_set(width: float, height: float) -> Dict[str, List[Path]]:
    w = width
    h = height
    return {
        'A': [
            Path(start=(0, 0), end=(w/2, h)),
            Path(start=(w/2, h), end=(w, 0)),
            Path(start=(w, 0), end=(3*w/4, h/2)),
        ],
        'B': [
            Path(start=(0, 0), end=(0, h)),
            Path(start=(0, h), end=(3*w/4, h)),
            Path(start=(3*w/4, h), end=(w, 7*h/8)),
            Path(start=(w, 7*h/8), end=(w, 5*h/8)),
            Path(start=(w, 5*h/8), end=(3*w/4, h/2)),
            Path(start=(3*w/4, h/2), end=(0, h/2)),
            Path(start=(0, h/2), end=(w, 3*h/8)),
            Path(start=(w, 3*h/8), end=(w, h/8)),
            Path(start=(w, h/8), end=(3*w/4, 0)),
            Path(start=(3*w/4, 0), end=(0, 0)),
        ],
        'C': [
            Path(start=(0, 0), end=(3*w/4, 0)),
            Path(start=(3*w/4, 0), end=(w/4, 0)),
            Path(start=(w/4, 0), end=(0, h/8)),
            Path(start=(0, h/8), end=(0, 7*h/8)),
            Path(start=(0, 7*h/8), end=(w/4, h)),
            Path(start=(w/4, h), end=(3*w/4, h)),
            Path(start=(3*w/4, h), end=(w, 7*h/8)),
        ],
        'D': [
            Path(start=(0, 0), end=(0, h)),
            Path(start=(0, h), end=(3*w/4, h)),
            Path(start=(3*w/4, h), end=(w, 7*h/8)),
            Path(start=(w, 7*h/8), end=(w, h/8)),
            Path(start=(w, h/8), end=(3*w/4, 0)),
            Path(start=(3*w/4, 0), end=(0, 0)),
        ],
        'E': [
            Path(start=(0, 0), end=(0, 0)),
            Path(start=(0, 0), end=(0, h/2)),
            Path(start=(0, h/2), end=(w, h/2)),
            Path(start=(w, h/2), end=(0, h)),
            Path(start=(0, h), end=(w, h)),
        ],
        'F': [
            Path(start=(0, 0), end=(0, h/2)),
            Path(start=(0, h/2), end=(w, h/2)),
            Path(start=(w, h/2), end=(0, h)),
            Path(start=(0, h), end=(w, h)),
        ],
        'G': [
            Path(start=(0, 0), end=(w, h/2)),
            Path(start=(w, h/2), end=(w, h/8)),
            Path(start=(w, h/8), end=(3*w/4, 0)),
            Path(start=(3*w/4, 0), end=(w/4, 0)),
            Path(start=(w/4, 0), end=(0, h/8)),
            Path(start=(0, h/8), end=(0, 7*h/8)),
            Path(start=(0, 7*h/8), end=(w/4, h)),
            Path(start=(w/4, h), end=(3*w/4, h)),
            Path(start=(3*w/4, h), end=(w, 7*h/8)),
        ],
        'H': [
            Path(start=(0, 0), end=(0, h)),
            Path(start=(0, h), end=(w, h/2)),
            Path(start=(w, h/2), end=(w, h)),
        ],
        'I': [
            Path(start=(0, 0), end=(w, h)),
            Path(start=(w, h), end=(w/2, 0)),
            Path(start=(w/2, 0), end=(w, 0)),
        ],
        'J': [
            Path(start=(0, 0), end=(w, h/8)),
            Path(start=(w, h/8), end=(w, h/8)),
            Path(start=(w, h/8), end=(3*w/4, 0)),
            Path(start=(3*w/4, 0), end=(w/4, 0)),
            Path(start=(w/4, 0), end=(0, h/8)),
        ],
        'K': [
            Path(start=(0, 0), end=(0, h)),
            Path(start=(0, h), end=(w, 0)),
            Path(start=(w, 0), end=(w, h)),
        ],
        'L': [
            Path(start=(0, 0), end=(0, 0)),
            Path(start=(0, 0), end=(0, h))
        ],
        'M': [
            Path(start=(0, 0), end=(0, h)),
            Path(start=(0, h), end=(w/2, h/2)),
            Path(start=(w/2, h/2), end=(w, h)),
            Path(start=(w, h), end=(w, 0)),
        ],
        'N': [
            Path(start=(0, 0), end=(0, h)),
            Path(start=(0, h), end=(w, 0)),
            Path(start=(w, 0), end=(w, h)),
        ],
        'O': [
            Path(start=(0, 0), end=(0, 7*h/8)),
            Path(start=(0, 7*h/8), end=(w/4, h)),
            Path(start=(w/4, h), end=(3*w/4, h)),
            Path(start=(3*w/4, h), end=(w, 7*h/8)),
            Path(start=(w, 7*h/8), end=(w, h/8)),
            Path(start=(w, h/8), end=(3*w/4, 0)),
            Path(start=(3*w/4, 0), end=(w/4, 0)),
            Path(start=(w/4, 0), end=(0, h/8)),
        ],
        'P': [
            Path(start=(0, 0), end=(0, h)),
            Path(start=(0, h), end=(3*w/4, h)),
            Path(start=(3*w/4, h), end=(w, 7*h/8)),
            Path(start=(w, 7*h/8), end=(w, 5*h/8)),
            Path(start=(w, 5*h/8), end=(3*w/4, h/2)),
            Path(start=(3*w/4, h/2), end=(0, h/2)),
        ],
        'Q': [
            Path(start=(0, 0), end=(w, 0)),
            Path(start=(w, 0), end=(0, 7*h/8)),
            Path(start=(0, 7*h/8), end=(w/4, h)),
            Path(start=(w/4, h), end=(3*w/4, h)),
            Path(start=(3*w/4, h), end=(w, 7*h/8)),
            Path(start=(w, 7*h/8), end=(w, h/8)),
            Path(start=(w, h/8), end=(3*w/4, 0)),
            Path(start=(3*w/4, 0), end=(w/4, 0)),
            Path(start=(w/4, 0), end=(0, h/8)),
        ],
        'R': [
            Path(start=(0, 0), end=(0, h)),
            Path(start=(0, h), end=(3*w/4, h)),
            Path(start=(3*w/4, h), end=(w, 7*h/8)),
            Path(start=(w, 7*h/8), end=(w, 5*h/8)),
            Path(start=(w, 5*h/8), end=(3*w/4, h/2)),
            Path(start=(3*w/4, h/2), end=(0, h/2)),
            Path(start=(0, h/2), end=(w, 0)),
        ],
        'S': [
            Path(start=(0, 0), end=(w/4, 0)),
            Path(start=(w/4, 0), end=(3*w/4, 0)),
            Path(start=(3*w/4, 0), end=(w, h/8)),
            Path(start=(w, h/8), end=(w, 3*h/8)),
            Path(start=(w, 3*h/8), end=(3*w/4, h/2)),
            Path(start=(3*w/4, h/2), end=(w/4, h/2)),
            Path(start=(w/4, h/2), end=(0, 5*h/8)),
            Path(start=(0, 5*h/8), end=(0, 7*h/8)),
            Path(start=(0, 7*h/8), end=(w/4, h)),
            Path(start=(w/4, h), end=(3*w/4, h)),
            Path(start=(3*w/4, h), end=(w, 7*h/8)),
        ],
        'T': [
            Path(start=(0, 0), end=(0, h)),
            Path(start=(0, h), end=(w, h)),
            Path(start=(w, h), end=(w, 7*h/8)),
            Path(start=(w, 7*h/8), end=(w/2, 0)),
        ],
        'U': [
            Path(start=(0, 0), end=(w, h/8)),
            Path(start=(w, h/8), end=(3*w/4, 0)),
            Path(start=(3*w/4, 0), end=(w/4, 0)),
            Path(start=(w/4, 0), end=(0, h/8)),
            Path(start=(0, h/8), end=(0, h)),
        ],
        'V': [
            Path(start=(0, 0), end=(w/2, 0)),
            Path(start=(w/2, 0), end=(w, h)),
        ],
        'W': [
            Path(start=(0, 0), end=(w/4, 0)),
            Path(start=(w/4, 0), end=(w/2, h/2)),
            Path(start=(w/2, h/2), end=(3*w/4, 0)),
            Path(start=(3*w/4, 0), end=(w, h)),
        ],
        'X': [
            Path(start=(0, 0), end=(w, h)),
            Path(start=(w, h), end=(w, 0)),
        ],
        'Y': [
            Path(start=(0, 0), end=(w/2, h/2)),
            Path(start=(w/2, h/2), end=(w, h)),
            Path(start=(w, h), end=(w/2, 0)),
        ],
        'Z': [
            Path(start=(0, 0), end=(w, h)),
            Path(start=(w, h), end=(0, 0)),
            Path(start=(0, 0), end=(w, 0)),
            Path(start=(w, 0), end=(3*w/4, h/2)),
        ],
        ' ': [],
        '!': [
            Path(start=(0, 0), end=(w/2, h/5)),
            Path(start=(w/2, h/5), end=(w/2, 0)),
        ],
        '?': [],
        'DEBUG': [
            Path(start=(0, 0), end=(0, h)),
            Path(start=(0, h), end=(w, h)),
            Path(start=(w, h), end=(w, 0)),
            Path(start=(w, 0), end=(0, 0)),
        ],
    }
