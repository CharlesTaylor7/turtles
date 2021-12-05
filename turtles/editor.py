from typing import Iterable
from turtle import Turtle, Vec2D

from turtles.utils import retreat, walk, add
from turtles.types import Path
from turtles.charset import character_set


def publish(turtle: Turtle, lines: Iterable[str]) -> None:
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
