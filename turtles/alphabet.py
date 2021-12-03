import math
from typing import List, Tuple, Callable, Optional, Dict, Union
from dataclasses import dataclass, field
from turtle import Turtle

from turtles.utils import copy_turtle, retreat, walk, ellipse



__all__ = ['write']

def write(turtle: Turtle, phrase: str) -> None:
    #ellipse(turtle, 50, 75, clockwise=True)

    phrase = 'BA' # delete this
    # phrase = 'BA' # delete this

    # character width
    width = 50
    # space between characters
    margin = 10
    characters = character_set(width=float(width))

    for c in phrase:
        strokes = characters[c]
        # turtles initial absolute position
        p = turtle.position()
        for s in strokes:
            if s.offset:
                walk(turtle, p + s.offset)
            turtle.setheading(s.heading)
            print(f'taking path {s.path} {s.args} {s.kwargs}')
            if isinstance(s.path, str):
                getattr(turtle, s.path)(*s.args, **s.kwargs)
            else:
                s.path(turtle, *s.args, **s.kwargs)

    retreat(turtle)


@dataclass
class Stroke:
    # initial heading
    heading: float
    # path to follow and its args
    # path is a string attribute which should be callable on the turtle class
    path: Union[str, Callable]
    args: tuple
    kwargs: Optional[dict] = field(default_factory=dict)

    # relative offset from the turtle's starting position
    # none indicates to resume from whereever it is
    offset: Optional[Tuple[int, int]] = None


def character_set(width: float) -> Dict[str, List[Stroke]]:
    s = width
    bh = 1.5*s
    return dict(
        A=[
            Stroke(heading=60, path='forward', args=(s,)),
            Stroke(heading=-60, path='forward', args=(s,)),
            Stroke(offset=(s/4, (s/4) * math.sqrt(3)), heading=0, path='forward', args=(s/2,)),
        ],
        B=[
            Stroke(heading=90, path='forward', args=(bh,)),
            Stroke(heading=0, path=ellipse, args=(bh/4, bh, 180), kwargs=dict(clockwise=True)),
            Stroke(heading=0, path=ellipse, args=(bh/4, bh, 180), kwargs=dict(clockwise=True)),
        ],
    )
