from datetime import datetime
from dataclasses import dataclass
from turtle import Turtle, getscreen, ontimer, mainloop


# init
screen = getscreen()
screen.bgcolor('black')

radius = 200
hour_hand_length = radius * 3 / 4


@dataclass
class TurtleHand:
    turtle: Turtle
    undo_offset: int

    def reset(self) -> None:
        while self.turtle.undobufferentries() - self.undo_offset:
            self.turtle.undo()


def make_turtle(speed: int) -> Turtle:
    t = Turtle('turtle')
    color = 'green'
    t.fillcolor(color)
    t.pencolor(color)
    t.pensize(5)
    t.speed(speed)
    return t


def redraw_hour_hand(hand: TurtleHand, seconds: int) -> None:
    hand.reset()
    hours = seconds // 3600
    t_h = hand.turtle
    t_h.showturtle()
    t_h.setheading(90 - 30 * hours)
    t_h.forward(hour_hand_length)
    t_h.penup()
    t_h.forward(2 * radius - hour_hand_length)
    t_h.hideturtle()


# hand functions
def redraw_minute_hand(hand: TurtleHand, seconds: int) -> None:
    minutes = seconds // 60
    hand.reset()
    turtle = hand.turtle
    turtle.showturtle()
    turtle.setheading(90 - 6 * minutes)
    turtle.forward(radius)
    turtle.penup()
    turtle.forward(radius)
    turtle.hideturtle()


def clock() -> None:
    # get current time
    time = datetime.now()
    s = time.second
    m = time.minute
    h = time.hour
    seconds = s + 60 * (m + 60 * h)

    # seconds hand
    t_s = make_turtle(9)
    t_s.setheading(90)
    t_s.penup()
    t_s.forward(radius)
    t_s.setheading(0)
    t_s.pendown()
    t_s.circle(-radius)
    t_s.setheading(-90)
    t_s.penup()
    t_s.forward(radius)
    t_s.pendown()
    t_s.setheading(90 - 6 * s)

    # hours hand
    copy = t_s.clone()
    copy.hideturtle()
    copy.speed(1)
    t_h = TurtleHand(turtle=copy, undo_offset=copy.undobufferentries())
    redraw_hour_hand(t_h, seconds)

    # minutes hand
    copy = t_s.clone()
    copy.hideturtle()
    copy.speed(1)
    t_m = TurtleHand(turtle=copy, undo_offset=copy.undobufferentries())
    redraw_minute_hand(t_m, seconds)

    def tick() -> None:
        nonlocal seconds
        seconds += 1
        if seconds % 3600 == 0:
            redraw_hour_hand(t_h, seconds)

        if seconds % 60 == 0:
            redraw_minute_hand(t_m, seconds)

        t_s.right(6)
        ontimer(tick, 100)
    tick()


clock()
mainloop()
