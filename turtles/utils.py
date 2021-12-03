from turtle import Turtle
import random


__all__ = ['new_turtle', 'copy_turtle', 'place']


def new_turtle(x, y, heading=0, speed='slowest') -> Turtle:
    t = Turtle(shape='turtle')
    t.setundobuffer(None)
    t.speed(speed)
    place(t, x, y, heading)
    return t


def copy_turtle(turtle: Turtle) -> Turtle:
    (x, y) = turtle.position()
    copy = new_turtle(x, y, heading=turtle.heading(), speed=turtle.speed())
    copy.fillcolor(turtle.fillcolor())
    copy.pencolor(turtle.pencolor())
    copy.pensize(turtle.pensize())
    return copy


def place(turtle: Turtle, x, y, heading) -> None:
    current_speed = turtle.speed()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.speed(current_speed)


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
