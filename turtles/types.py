from typing import Literal, Tuple
from dataclasses import dataclass


Point = Tuple[float, float]


@dataclass
class Path:
    start: Point
    end: Point


TurtleSpeed = Literal[
    'slowest', 'slow', 'normal', 'fast', 'fastest',
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]
