import math
from typing import List, Tuple, Callable, Optional, Dict
from dataclasses import dataclass
from turtle import Turtle

from turtles.utils import copy_turtle, retreat, walk



__all__ = ['write']

def write(turtle: Turtle, phrase: str) -> None:
    phrase = 'A' # delete this

    for c in phrase:
        strokes = characters[c]
        # turtles initial absolute position
        p = turtle.position()
        for s in strokes:
            if s.offset:
                walk(turtle, p + s.offset)
            turtle.setheading(s.heading)
            print(f'taking path {s.path} {s.args}')
            getattr(turtle, s.path)(*s.args)

    retreat(turtle)


@dataclass
class Stroke:
    # initial heading
    heading: float
    # path to follow and its args
    # path is a string attribute which should be callable on the turtle class
    path: str
    args: Tuple

    # relative offset from the turtle's starting position
    # none indicates to resume from whereever it is
    offset: Optional[Tuple[int, int]] = None

characters: Dict[str, List[Stroke]] = dict(
    A=[
        Stroke(heading=60, path='forward', args=(50,)),
        Stroke(heading=-60, path='forward', args=(50,)),
        Stroke(offset=(12.5, 12.5 * math.sqrt(3)), heading=0, path='forward', args=(25,)),
    ],
)

def A(turtle):

    turtle.left(60)
    turtle.forward(50)
    copy = copy_turtle(turtle)
    copy.right(60)
    copy.forward(45)
    retreat(copy)
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(100)
    retreat(turtle)

