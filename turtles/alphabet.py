import math
from typing import List, Tuple, Callable, Optional, Dict, Union, Iterable, cast, Generic
from turtle import Turtle, Vec2D
from dataclasses import dataclass, field
from typeguard import typechecked
from adt import adt, Case

from turtles.utils import retreat, walk, ellipse, to_radians, line, circle, vector
from turtles.config import settings


__all__ = ['write']


def write(turtle: Turtle, lines: Iterable[str]) -> None:
    # character width
    width = 100
    # space between characters
    margin = 20
    characters = character_set(width=float(width))
    shift = width + margin
    # (x, y) = (-600, 300)
    (x, y) = (-200, 100)
    for (j, phrase) in enumerate(lines):
        for (i, c) in enumerate(phrase):
            print(f'drawing \'{c}\'')
            strokes = characters.get(c)
            if strokes is None:
                print(f'skipping undefined \'{c}\'')
                continue

            # walk to next character
            walk(turtle, (x + i * shift, y - j * shift))

            # turtles initial position for this character
            p: Vec2D = turtle.position()

            def apply_stroke(s: Stroke) -> None:
                if s.offset:
                    (x, y) = s.offset
                    walk(turtle, add(p, vector(x, y)))

                print(f'heading at {s.heading}')
                turtle.setheading(s.heading)

                print(f'taking path {s.path.__name__} {s.kwargs}')
                s.path(turtle, **s.kwargs)

            if settings.draw_debug_box:
                for s in characters['DEBUG']:
                    apply_stroke(s)

            for s in strokes:
                apply_stroke(s)

    retreat(turtle)


@typechecked
def add(a: Vec2D, b: Vec2D) -> Vec2D:
    # Vec2D has an overriden + operator which performs vector addition
    return a + b  # type: ignore[return-value]


@dataclass
class Stroke:
    # initial heading
    heading: float
    # path to follow and its args
    # path is a string attribute which should be callable on the turtle class
    path: Callable[..., None]
    kwargs: dict

    # relative offset from the turtle's starting position
    # none indicates to resume from whereever it is
    offset: Optional[Tuple[float, float]] = None


def character_set(width: float) -> Dict[str, List[Stroke]]:
    w = width
    h = width
    s = width
    # incline of the letters A, & V
    a = 70
    # hypotneuse of the letters A & V
    a_r = s / math.sin(to_radians(a))
    # width under 1 stroke of A or V
    a_w = s * math.tan(to_radians(90-a))
    # relative shift to the right for the whole letter (A & V)
    a_x = (s - 2 * a_w) / 2

    # angle of the letter W
    W_heading = 76
    W_th = to_radians(W_heading)
    W_r = s / math.sin(W_th)
    # x displacement under 1 stroke of the W
    W_x = s * math.tan(to_radians(90 - W_heading))
    # relative x shift for the whole letter
    W_shift_x = (s - 4 * W_x) / 2

    # M
    M_heading = 55
    M_th = to_radians(M_heading)
    M_r = s / math.sin(M_th)
    M_x = s * math.tan(to_radians(90 - M_heading))
    M_shift_x = (s - M_x) / 2
    return {
        'A': [
            Stroke(heading=a, offset=(a_x, 0), path=line, kwargs=dict(distance=a_r)),
            Stroke(heading=-a, path=line, kwargs=dict(distance=a_r)),
            Stroke(heading=0, offset=(a_x + a_w/2, a_r/2), path=line, kwargs=dict(distance=a_w)),
        ],
        'B': [
            Stroke(heading=90, path=line, kwargs=dict(distance=s)),
            Stroke(heading=0, path=circle, kwargs=dict(radius=s/4, extent=180, clockwise=True)),
            Stroke(heading=0, path=circle, kwargs=dict(radius=s/4, extent=180, clockwise=True)),
        ],
        'E': [
            Stroke(heading=180, offset=(3*w/4, 0), path=line, kwargs=dict(distance=w/2)),
            Stroke(heading=90, path=line, kwargs=dict(distance=h/2)),
            Stroke(heading=0, path=line, kwargs=dict(distance=w/2)),
            Stroke(heading=90, offset=(w/4, h/2), path=line, kwargs=dict(distance=h/2)),
            Stroke(heading=0, path=line, kwargs=dict(distance=w/2)),
        ],
        'F': [
            Stroke(heading=180, offset=(3*w/4, 0), path=line, kwargs=dict(distance=w/2)),
            Stroke(heading=90, path=line, kwargs=dict(distance=h/2)),
            Stroke(heading=0, path=line, kwargs=dict(distance=w/2)),
            Stroke(heading=90, offset=(w/4, h/2), path=line, kwargs=dict(distance=h/2)),
            Stroke(heading=0, path=line, kwargs=dict(distance=w/2)),
        ],
        'G': [
            Stroke(
                heading=135, path=circle, kwargs=dict(radius=s/2, extent=315),
                offset=(s/2 * (1 + 1/math.sqrt(2)), (s/2) * (1 + 1/math.sqrt(2))),
            ),
            Stroke(heading=180, path=line, kwargs=dict(distance=s/2)),
        ],
        'M': [
            Stroke(heading=90, offset=(M_shift_x, 0), path=line, kwargs=dict(distance=s)),
            Stroke(heading=-M_heading, path=line, kwargs=dict(distance=M_r/2)),
            Stroke(heading=M_heading, path=line, kwargs=dict(distance=M_r/2)),
            Stroke(heading=-90, path=line, kwargs=dict(distance=s)),
        ],
        'O': [
            Stroke(heading=0, offset=(s/2, 0), path=circle, kwargs=dict(radius=s/2)),
        ],
        'P': [
            Stroke(heading=90, path=line, kwargs=dict(distance=s)),
            Stroke(heading=0, path=circle, kwargs=dict(radius=s/4, extent=180, clockwise=True)),
        ],
        'R': [
            Stroke(heading=90, path=line, kwargs=dict(distance=s)),
            Stroke(heading=0, path=circle, kwargs=dict(radius=s/4, extent=180, clockwise=True)),
            Stroke(heading=-0.75 * 90, path=line, kwargs=dict(distance=s/2)),
        ],
        'S': [
            Stroke(heading=-90, offset=(s/4, s/8), path=line, kwargs=dict(distance=s/8)),
            Stroke(heading=0, path=line, kwargs=dict(distance=s/2)),
            Stroke(heading=90, path=line, kwargs=dict(distance=s/2)),
            Stroke(heading=180, path=line, kwargs=dict(distance=s/2)),
            Stroke(heading=90, path=line, kwargs=dict(distance=s/2)),
            Stroke(heading=0, path=line, kwargs=dict(distance=s/2)),
            Stroke(heading=-90, path=line, kwargs=dict(distance=s/8)),
        ],
        'T': [
            Stroke(heading=0, offset=(0, s), path=line, kwargs=dict(distance=s)),
            Stroke(heading=-90, offset=(s/2, s), path=line, kwargs=dict(distance=s)),
        ],
        'U': [
            Stroke(heading=-90, offset=(s, s), path=ellipse, kwargs=dict(a=s/2, b=s, extent=180, clockwise=True))
        ],

        'V': [
            Stroke(heading=-a, offset=(a_x, s), path=line, kwargs=dict(distance=a_r)),
            Stroke(heading=a, path=line, kwargs=dict(distance=a_r)),
        ],
        'W': [
            Stroke(heading=-W_heading, offset=(W_shift_x, s), path=line, kwargs=dict(distance=W_r)),
            Stroke(heading=W_heading, path=line, kwargs=dict(distance=W_r)),
            Stroke(heading=-W_heading, path=line, kwargs=dict(distance=W_r)),
            Stroke(heading=W_heading, path=line, kwargs=dict(distance=W_r)),
        ],
        ' ': [],
        '!': [
            Stroke(heading=-90, offset=(s/2, s), path=line, kwargs=dict(distance=8*s/10)),
            Stroke(heading=90, offset=(s/2, 0), path=line, kwargs=dict(distance=s/20)),
        ],
        '?': [
        ],
        'DEBUG': [
            Stroke(heading=90, path=line, kwargs=dict(distance=s)),
            Stroke(heading=0, path=line, kwargs=dict(distance=s)),
            Stroke(heading=-90, path=line, kwargs=dict(distance=s)),
            Stroke(heading=180, path=line, kwargs=dict(distance=s)),
        ],
    }
