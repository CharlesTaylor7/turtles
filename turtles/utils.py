import math
import random

from typing import Optional, Tuple, Literal, Union
from turtle import Turtle, ontimer


__all__ = ['new_turtle', 'copy_turtle']


TurtleSpeed = Literal[
    'slowest', 'slow', 'normal', 'fast', 'fastest',
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]


def new_turtle(
    color: str,
    size: int,
    x: float = 0,
    y: float = 0,
    heading: Optional[float] = None,
    speed: TurtleSpeed = 'slowest',
    teleport: bool = False,
) -> Turtle:
    print(f'Turtle {x=}, {y=}, {color=}, {size=}, {speed=}, {teleport=}')
    t = Turtle(shape='turtle')
    t.setundobuffer(None)
    t.fillcolor(color)
    t.pencolor(color)
    t.pensize(size)
    t.speed(speed)
    t.speed(10) # delete this
    position(t, x, y, heading, teleport=teleport)
    return t


def copy_turtle(turtle: Turtle) -> Turtle:
    (x, y) = turtle.position()
    return new_turtle(
        x=x,
        y=y,
        color=turtle.fillcolor(),
        size=turtle.pensize(),
        heading=turtle.heading(),
        speed=turtle.speed(), # type: ignore[arg-type]
        teleport=True,
    )


def position(turtle: Turtle, x: float, y: float, heading: Optional[float], teleport: bool) -> None:
    if teleport:
        current_speed = turtle.speed()
        turtle.speed(0)
    else:
        print(f'walking to {(x, y)}')
        turtle.setheading(turtle.towards(x, y))

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    if teleport:
        turtle.speed(current_speed)

    if heading is not None:
        turtle.setheading(heading)


def retreat(turtle: Turtle) -> None:
    walk(turtle, (0, 0))
    turtle.hideturtle()


def walk(turtle: Turtle, position: Tuple[float, float]) -> None:
    """
    walk without drawing
    """
    print(f'walking to {position}')
    (x, y) = position
    turtle.penup()
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    turtle.pendown()


def spin(turtle: Turtle) -> None:
    turtle.left(random.randint(1, 360))


def nudge(turtle: Turtle) -> None:
    def move() -> None:
        turtle.forward(10)
        ontimer(move, 400)
    move()


def ellipse(turtle: Turtle, a: float, b: float, extent: float = 360, clockwise: bool = False) -> None:
    """
    https://stackoverflow.com/a/61985797
    TODO: make this start the ellipse tangent to the turtles current heading
    """
    # ellipse takes a while to draw, so temporarily override speed
    speed = turtle.speed()
    turtle.speed('fastest')

    print(f'drawing ellipse {a=}, {b=}, {extent=}, {clockwise=}')
    sign = -1 if clockwise else 1

    d = 10
    num_steps = int(d * extent / 360.0)

    # drawing
    (p_x, k) = turtle.position()
    h = p_x - a
    for n in range(num_steps + 1):
        t = (n/d) * 2 * math.pi
        x = h + a * math.cos(t)
        y = k + b * math.sin(t) * sign
        turtle.setheading(turtle.towards(x,y))
        turtle.goto(x, y)

    turtle.speed(speed)


def to_radians(degrees: float) -> float:
    return math.pi * degrees / 180


def forward(turtle: Turtle, pixels: float) -> None:
    turtle.forward(pixels)

def circle(turtle: Turtle, radius: float, extent: Optional[float] = None) -> None:
    turtle.circle(radius, extent)
