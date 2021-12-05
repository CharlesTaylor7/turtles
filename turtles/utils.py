import math
import random

from typing import Optional, Tuple, Literal, Union
from turtle import Turtle, ontimer, Vec2D

from turtles.config import settings
from turtles.types import TurtleSpeed


__all__ = ['new_turtle', 'copy_turtle']


def new_turtle(
    color: str,
    size: int,
    x: float = 0,
    y: float = 0,
    heading: Optional[float] = None,
    speed: TurtleSpeed = settings.turtle_speed,
    teleport: bool = False,
) -> Turtle:
    print(f'Turtle {x=}, {y=}, {color=}, {size=}, {speed=}, {teleport=}')
    t = Turtle(shape='turtle')
    t.setundobuffer(None)
    t.fillcolor(color)
    t.pencolor(color)
    t.turtlesize(size)
    t.pensize(size)
    t.speed(speed)
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
        speed=turtle.speed(),  # type: ignore[arg-type]
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

def set_color(turtle: Turtle, color: str) -> None:
    turtle.pencolor(color)
    turtle.fillcolor(color)


def dance(turtle: Turtle) -> None:
    motion = 30
    interval = 400
    # move to initial position
    turtle.setheading(90 + motion / 2)
    def left() -> None:
        set_color(turtle, 'magenta')
        turtle.left(motion)
        ontimer(right, interval)

    def right() -> None:
        set_color(turtle, 'cyan')
        turtle.right(motion)
        ontimer(left, interval)
    right()


def to_radians(degrees: float) -> float:
    return math.pi * degrees / 180


def line(turtle: Turtle, *, distance: float) -> None:
    turtle.forward(distance)


def circle(turtle: Turtle, *, radius: float, extent: float, clockwise: bool) -> None:
    if clockwise:
        radius = -radius
    turtle.circle(radius, extent)


def ellipse(turtle: Turtle, *, a: float, b: float, extent: float = 360, clockwise: bool = False) -> None:
    """
    https://stackoverflow.com/a/61985797
    TODO: make this start the ellipse tangent to the turtles current heading
    """
    # ellipse takes a while to draw, so temporarily override speed
    speed = turtle.speed()
    turtle.speed('fastest')
    theta = to_radians(turtle.heading() - 90)

    print(f'drawing ellipse {a=}, {b=}, {extent=}, {clockwise=}')
    sign = -1 if clockwise else 1

    d = 10
    num_steps = int(d * extent / 360.0)

    # drawing
    (p_x, p_y) = turtle.position()
    h = p_x - a
    k = p_y
    for n in range(num_steps + 1):
        t = (n/d) * 2 * math.pi
        x = h + a * math.cos(t)
        y = k + b * math.sin(t) * sign
        (x, y) = rotate(vector(x, y), theta)
        turtle.setheading(turtle.towards(x, y))
        turtle.goto(x, y)

    turtle.speed(speed)


def rotate(v: Vec2D, theta: float) -> Vec2D:
    (x, y) = v
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    return vector(x * cos_theta - y * sin_theta, x * sin_theta + y * cos_theta)


def vector(x: float, y: float) -> Vec2D:
    # mypy does not believe Vec2D is a callable constructor
    return Vec2D(x, y)  # type: ignore[operator]
