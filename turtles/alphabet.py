import math
from typing import List, Tuple, Callable, Optional, Dict, Union, Iterable, cast
from dataclasses import dataclass, field
from turtle import Turtle, Vec2D

from turtles.utils import copy_turtle, retreat, walk, ellipse



__all__ = ['write']

def write(turtle: Turtle, phrase: str) -> None:
    # enable this
    # walk(turtle, -100, 100) 
    phrase: Iterable[str] = set(phrase) # delete this
    print(f'writing {phrase}') # delete this

    # character width
    width = 50
    # space between characters
    margin = 10
    characters = character_set(width=float(width))

    for c in phrase:
        print(f'drawing \'{c}\'')
        strokes = characters[c]
        # turtles initial for this character 
        p = turtle.position()

        for s in strokes:
            if s.offset:
                walk(turtle, cast(Vec2D, p + s.offset))
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
    kwargs: dict = field(default_factory=dict)

    # relative offset from the turtle's starting position
    # none indicates to resume from whereever it is
    offset: Optional[Tuple[float, float]] = None


def character_set(width: float) -> Dict[str, List[Stroke]]:
    s = width
    bh = 1.5*s
    return {
        'A': [
            Stroke(heading=60, path='forward', args=(s,)),
            Stroke(heading=-60, path='forward', args=(s,)),
            Stroke(offset=(s/4, (s/4) * math.sqrt(3)), heading=0, path='forward', args=(s/2,)),
        ],
        'B': [
            Stroke(heading=90, path='forward', args=(bh,)),
            Stroke(heading=0, path=ellipse, args=(bh/4, bh, 180), kwargs=dict(clockwise=True)),
            Stroke(heading=0, path=ellipse, args=(bh/4, bh, 180), kwargs=dict(clockwise=True)),
        ],
        'E': [
        ],
        'G': [
            Stroke(heading=180-45, path='circle', args=(s,270+45,)),
            Stroke(heading=180, path='forward', args=(s,)),
        ],
        'O': [
        ],
        'T': [
        ],
        'U': [
        ],
        ' ': [
            Stroke(heading=0, path='forward', args=(width,)),
        ],
        '!': [
            Stroke(heading=90, path='forward', args=(s/10,)),
            Stroke(heading=90, path=walk, args=(s/10,)),
            Stroke(heading=90, path='forward', args=(8*s/10,)),
        ],
        '?': [
        ],
    }
