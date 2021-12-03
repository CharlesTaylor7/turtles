import math
import random

from typing import Optional, Tuple
from turtle import Turtle


__all__ = ['new_turtle', 'copy_turtle']


def new_turtle(
    color,
    size,
    x: float = 0,
    y: float = 0,
    heading=None,
    speed='slowest',
    teleport=False,
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
        x,
        y,
        color=turtle.fillcolor(),
        size=turtle.pensize(),
        heading=turtle.heading(),
        speed=turtle.speed(),
        teleport=True,
    )


def position(turtle: Turtle, x, y, heading: Optional[float], teleport) -> None:
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


def retreat(turtle: Turtle):
    walk(turtle, (0, 0))
    turtle.hideturtle()


def walk(turtle: Turtle, position: Tuple[float, float]):
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
    def move():
        turtle.forward(10)
        ontimer(move, 400)
    move()


def ellipse(turtle, a, b, extent=360, clockwise=False):
    """
    https://stackoverflow.com/a/61985797
    TODO: make this start the ellipse tangent to the turtles current heading
    """
    # ellipse takes a while to draw, so temporarily override speed
    speed = turtle.speed()
    turtle.speed('fastest')

    print(f'drawing ellipse {a=}, {b=}, {extent=}, {clockwise=}')
    sign = -1 if clockwise else 1

    # We are multiplying by 0.875 because for making a complete ellipse we are plotting 315 pts according
    converted_angle = int(extent * 0.875)

    # drawing
    (h, k) = turtle.position() - (a, 0)
    for i in range(converted_angle + 1):
        x = h + a * math.cos(i/50)
        y = k + b * math.sin(i/50) * sign
        turtle.setheading(turtle.towards(x,y))
        turtle.goto(x, y)

    turtle.speed(speed)
