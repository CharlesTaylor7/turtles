from queue import Queue
import threading
import turtle


# multi threading example:
# https://stackoverflow.com/a/44833522
def push_command(handler, *args, **kwargs):
    command_queue.put((handler, args, kwargs))

def tes1():
    for _ in range(360):
        push_command(turtle1.forward, 20)
        push_command(turtle1.left, 1)

def tes2():
    for _ in range(360):
        push_command(turtle2.forward, 1)
        push_command(turtle2.right, 1)

def process_queue():
    while not command_queue.empty():
        handler, args, kwargs = command_queue.get()
        handler(*args, **kwargs)


    if threading.active_count() > 1:
        turtle.ontimer(process_queue, 100)

command_queue = Queue(1)  # size = number of hardware threads you have - 1

turtle1 = turtle.Turtle('turtle')
turtle1.speed('fastest')
thread1 = threading.Thread(target=tes1)
thread1.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread1.start()

turtle2 = turtle.Turtle('turtle')
turtle2.speed('fastest')
thread2 = threading.Thread(target=tes2)
thread2.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
# thread2.start()

process_queue()

turtle.mainloop()
