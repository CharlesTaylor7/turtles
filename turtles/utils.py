from typing import Optional, Tuple
from turtle import Turtle
import random


__all__ = ['new_turtle', 'copy_turtle']


def new_turtle(
    x,
    y,
    color,
    size,
    heading=None,
    speed='slowest',
    teleport=False,
) -> Turtle:
    t = Turtle(shape='turtle')
    t.setundobuffer(None)
    t.fillcolor(color)
    t.pencolor(color)
    t.pensize(size)
    t.speed(speed)
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


def retreat(turtle):
    walk(turtle, (0, 0))
    turtle.hideturtle()

def walk(turtle, position: Tuple[int, int]):
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

def circle(turtle: Turtle) -> None:
    for _ in range(360):
        turtle.forward(1)
        turtle.left(1)
