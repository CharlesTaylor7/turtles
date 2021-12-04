from dataclasses import dataclass

from turtles.types import TurtleSpeed


@dataclass
class Config:
    turtle_speed: TurtleSpeed = 'normal'
    draw_debug_box: bool = False


settings = Config()
