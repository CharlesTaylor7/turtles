import math
import random

from typing import Optional, Callable
from turtle import Turtle, ontimer, Vec2D
from typeguard import typechecked

from turtles.config import settings
from turtles.types import TurtleSpeed, Point


def new_turtle(
    color: str = 'green',
    pen_size: int = 1,
    turtle_size: int = 1,
    x: float = 0,
    y: float = 0,
    heading: Optional[float] = None,
    speed: TurtleSpeed = 'normal',
    teleport: bool = False,
) -> Turtle:
    t = Turtle(shape='turtle')
    t.fillcolor(color)
    t.pencolor(color)
    t.pensize(pen_size)
    t.turtlesize(turtle_size)
    t.speed(speed if settings.override_turtle_speed is None else settings.override_turtle_speed)
    position(t, x, y, heading, teleport=teleport)
    return t


def position(turtle: Turtle, x: float, y: float, heading: Optional[float], teleport: bool) -> None:
    if teleport:
        current_speed = turtle.speed()
        turtle.speed(0)
    else:
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
    turtle.stop_turtle = dance(turtle)  # type: ignore


def walk(turtle: Turtle, position: Point) -> None:
    """
    walk without drawing
    """
    if turtle.position() == position:
        return

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


def dance(turtle: Turtle) -> Callable[[], None]:
    motion = 30
    interval = 400
    # move to initial position
    turtle.setheading(90 + motion / 2)
    cease = False

    def left() -> None:
        if cease:
            return
        set_color(turtle, 'magenta')
        turtle.left(motion)
        ontimer(right, interval)  # type: ignore

    def right() -> None:
        if cease:
            return
        set_color(turtle, 'cyan')
        turtle.right(motion)
        ontimer(left, interval)

    def stop() -> None:
        nonlocal cease
        cease = True

    right()
    return stop


def to_radians(degrees: float) -> float:
    return math.pi * degrees / 180


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


@typechecked
def add(a: Vec2D, b: Vec2D) -> Vec2D:
    # Vec2D has an overriden + operator which performs vector addition
    return a + b  # type: ignore[return-value]
