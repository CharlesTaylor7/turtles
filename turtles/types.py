from typing import Literal, Tuple


Point = Tuple[int, int]


TurtleSpeed = Literal[
    'slowest', 'slow', 'normal', 'fast', 'fastest',
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]
