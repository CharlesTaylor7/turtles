import math
from typing import List, Tuple, Callable, Optional, Dict, Union, Iterable, cast
from dataclasses import dataclass, field
from turtle import Turtle, Vec2D

from turtles.utils import copy_turtle, retreat, walk, ellipse



__all__ = ['write']

def write(turtle: Turtle, phrase: str) -> None:
    walk(turtle, (-400, 0))

    # character width
    width = 100
    height = 100
    # space between characters
    margin = 20
    characters = character_set(width=float(width), height=float(height))

    for c in phrase:
        print(f'drawing \'{c}\'')
        strokes = characters[c]

        # turtles initial for this character 
        p = turtle.position()

        def apply_stroke(s):
            if s.offset:
                walk(turtle, cast(Vec2D, p + s.offset))
            turtle.setheading(s.heading)
            print(f'taking path {s.path} {s.args} {s.kwargs}')

            # call method of turtle by looking up the attribute
            if isinstance(s.path, str):
                getattr(turtle, s.path)(*s.args, **s.kwargs)

            # call utility by using the passed callable
            else:
                s.path(turtle, *s.args, **s.kwargs)

        for s in characters['DEBUG']:
            apply_stroke(s)

        for s in strokes:
            apply_stroke(s)


        # advance to next character
        walk(turtle, p + (width + margin, 0))

    retreat(turtle)


@dataclass
class Stroke:
    # initial heading
    heading: float
    # path to follow and its args
    # path is a string attribute which should be callable on the turtle class
    path: Union[str, Callable]
    args: tuple = field(default_factory=tuple)
    kwargs: dict = field(default_factory=dict)

    # relative offset from the turtle's starting position
    # none indicates to resume from whereever it is
    offset: Optional[Tuple[float, float]] = None


def character_set(width: float, height: float) -> Dict[str, List[Stroke]]:
    w = width
    h = height

    s = width
    bh = 1.5*s
    return {
        'A': [
            Stroke(heading=60, path='forward', args=(s,)),
            Stroke(heading=-60, path='forward', args=(s,)),
            Stroke(heading=0, offset=(s/4, (s/4) * math.sqrt(3)), path='forward', args=(s/2,)),
        ],
        'B': [
            Stroke(heading=90, path='forward', args=(bh,)),
            Stroke(heading=0, path=ellipse, args=(bh/4, bh, 180), kwargs=dict(clockwise=True)),
            Stroke(heading=0, path=ellipse, args=(bh/4, bh, 180), kwargs=dict(clockwise=True)),
        ],
        'E': [
            Stroke(heading=180, offset=(3*w/4, 0), path='forward', args=(w/2,)),
            Stroke(heading=90, path='forward', args=(h/2,)),
            Stroke(heading=0, path='forward', args=(w/2,)),
            Stroke(heading=90, offset=(w/4, h/2), path='forward', args=(h/2,)),
            Stroke(heading=0, path='forward', args=(w/2,)),
        ],
        'G': [
            Stroke(heading=135, path='circle', args=(s/2,315,),
                offset=(s/2 * (1 + 1/math.sqrt(2)), (s/2) * (1 + 1/math.sqrt(2))),
            ),
            Stroke(heading=180, path='forward', args=(s/2,)),
        ],
        'O': [
            Stroke(heading=0, offset=(s/2, 0), path='circle', args=(s/2,360,)),
        ],
        'T': [
            Stroke(heading=0, offset=(0, s), path='forward', args=(s,)),
            Stroke(heading=-90, offset=(s/2, s), path='forward', args=(s,)),
        ],
        'U': [
            Stroke(heading=-90, offset=(s, s), path=ellipse, kwargs=dict(a=s/2, b=s, extent=180, clockwise=True))
        ],
        ' ': [],
        '!': [
            Stroke(heading=-90, offset=(s/2, s), path='forward', args=(8*s/10,)),
            Stroke(heading=90, offset=(s/2, 0), path='forward', args=(s/20,)),
        ],
        '?': [
        ],
        'DEBUG': [
            Stroke(heading=90, path='forward', args=(s,)),
            Stroke(heading=0, path='forward', args=(s,)),
            Stroke(heading=-90, path='forward', args=(s,)),
            Stroke(heading=180, path='forward', args=(s,)),
        ],
    }

def to_radians(degrees: float):
    return math.PI * degrees / 180
