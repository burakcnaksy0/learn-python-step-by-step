import turtle
import time
def draw_square():
    t=turtle.Turtle()
    for i in range(4):
        t.forward(100)
        t.right(90)
        time.sleep(2)
    turtle.done()

draw_square()        