from typing import Optional
from dataclasses import dataclass

from turtles.types import TurtleSpeed


@dataclass
class Config:
    override_turtle_speed: Optional[TurtleSpeed] = None
    draw_debug_box: bool = False


settings = Config(override_turtle_speed=0)
