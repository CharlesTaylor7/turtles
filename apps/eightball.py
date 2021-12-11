import random

from typing import Optional, Iterable, Any
from turtles.editor import publish
from turtles.utils import new_turtle, DancingTurtle, new_screen
from turtles.types import Screen

from turtle import mainloop, Turtle, textinput


answers = [
    ['we made it up'],
    ['pure fiction'],
    ['I am very small', 'so you can', 'imagine the kind', 'of stress', 'that I am under'],
    ['henlo fren'],
]


def shout(article: Iterable[str]) -> Iterable[str]:
    return (
        line.upper() for line in article
    )


def reset(turtle: DancingTurtle) -> None:
    turtle.stop_dancing()
    turtle.reset()
    turtle.speed(0)
    turtle.fillcolor('green')
    turtle.pencolor('green')
    turtle.pensize(3)


def on_click(screen: Screen, turtle: DancingTurtle) -> None:
    def wrapped(_x: float, _y: float) -> None:
        # ask for input
        phrase: Optional[str] = textinput('What is your question?', '')

        if phrase:
            reset(turtle)
            article = random.choice(answers)
            publish(turtle, shout(article))
            turtle.dance()

    screen.onclick(wrapped)


screen = new_screen(title='Click to speak to the wise turtle')
wise_turtle = new_turtle(DancingTurtle)
reset(wise_turtle)
wise_turtle.dance()
on_click(screen, wise_turtle)
mainloop()
