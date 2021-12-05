import random

from typing import Optional, Iterable, Any, Callable
from turtles.editor import publish
from turtles.utils import new_turtle, DancingTurtle

from turtle import mainloop, Turtle, Screen, textinput


answers = [
    ['we made it up',],
    ['pure fiction',],
    ['I am very small', 'so you can', 'imagine the kind', 'of stress', 'that I am under',],
    ['henlo fren',],
]



def shout(article: Iterable[str]) -> Iterable[str]:
    return (
        line.upper() for line in article
    )


def reset(turtle: Turtle) -> None:
    getattr(turtle, 'stop_dance', lambda: None)()
    turtle.reset()
    turtle.speed(0)
    turtle.fillcolor('green')
    turtle.pencolor('green')
    turtle.pensize(3)


def on_click(screen: Any, turtle: Turtle) -> None:
    def wrapped(_x: float, _y: float) -> None:
        # ask for input
        phrase: Optional[str] = textinput('What is your question?', '')

        if phrase:
            reset(turtle)
            article = random.choice(answers)
            publish(turtle, shout(article))
            turtle.stop_dance = dance(turtle)  # type: ignore

    screen.onclick(wrapped)


screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.title('Click to speak to the wise turtle')
wise_turtle = new_turtle(DancingTurtle)
reset(wise_turtle)
wise_turtle.dance()
on_click(screen, wise_turtle)
mainloop()
