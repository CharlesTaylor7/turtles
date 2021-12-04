from datetime import datetime
from turtle import Turtle, getscreen, ontimer, mainloop

# init
screen = getscreen()
screen.bgcolor('black')


def make_turtle(speed: int) -> Turtle:
    t = Turtle('turtle')
    color = 'green'
    t.fillcolor(color)
    t.pencolor(color)
    t.pensize(5)
    t.speed(speed)
    return t



def clock() -> None:
    radius = 200
    hour_hand_length = radius * 3 / 4

    # get current time
    time = datetime.now()
    s = time.second
    m = time.minute
    h = time.hour
    seconds = s + 60 * (m + 60 * h)
    print(f'{h=}, {m=}, {s=}, {seconds=}')

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
    t_h = t_s.clone()
    t_h.hideturtle()
    t_h.speed(1)
    t_h_undo_count = t_h.undobufferentries()

    def redraw_hour_hand() -> None:
        hours = seconds // 3600
        while t_h.undobufferentries() - t_h_undo_count:
            t_h.undo()
        t_h.showturtle()
        print(hours)
        t_h.setheading(90 - 30 * hours)
        t_h.forward(hour_hand_length)
        t_h.penup()
        t_h.forward(2 * radius - hour_hand_length)
        t_h.hideturtle()

    redraw_hour_hand()

    # minutes hand
    t_m = t_s.clone()
    t_m.hideturtle()
    t_m.speed(1)
    t_m_undo_count = t_m.undobufferentries()

    # hand functions
    def redraw_minute_hand() -> None:
        minutes = seconds // 60
        while t_m.undobufferentries() - t_m_undo_count:
            t_m.undo()
        t_m.showturtle()
        t_m.setheading(90 - 6 * minutes)
        t_m.forward(radius)
        t_m.penup()
        t_m.forward(radius)
        t_m.hideturtle()

    redraw_minute_hand()

    def tick() -> None:
        nonlocal seconds
        seconds += 1
        if seconds % 3600 == 0:
            redraw_hour_hand()

        if seconds % 60 == 0:
            redraw_minute_hand()

        t_s.right(6)
        ontimer(tick, 100)
    tick()


clock()
mainloop()
