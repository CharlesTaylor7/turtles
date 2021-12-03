import turtle
from turtle import Turtle, getscreen, mainloop, register_shape
import random

# ideas
# - on every click the turtle turns at random and moves 100 steps forward
# - turtle chases the mouse in real time
# - fleet of turtles
# - crazy shit, like turtles chasing each other while changing color and speeding up and slowing down randomly
# - Roomba: turtle moves in clean orderly lines up and down
# - every click spawns a new turtle

# set turtle shapes
turtle.addshape('turtle.gif')
turtle.shape('turtle.gif')

fleet = []

def main():
    screen = getscreen()
    screen.onclick(onClick)
    mainloop()

# num_clicks = 0

def onClick(x, y):
    fleet.append(Turtle())

    # global num_clicks
    # num_clicks += 1
    random_angle = random.randrange(1, 360, 1)
    turtle.right(random_angle)
    turtle.forward(100)


main()
