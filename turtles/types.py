from typing import Literal, Tuple
from dataclasses import dataclass
from turtle import Vec2D, Turtle

from turtles import utils


Point = Tuple[float, float]


@dataclass
class Path:
    start: Point
    end: Point

    def shift(self, vector: Vec2D) -> 'Path':
        return Path(vector + self.start, vector + self.end)  # type: ignore


    def draw(self, turtle: Turtle) -> None:
        utils.walk(turtle, self.start)
        turtle.setheading(turtle.towards(self.end))
        turtle.goto(self.end)


TurtleSpeed = Literal[
    'slowest', 'slow', 'normal', 'fast', 'fastest',
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]
