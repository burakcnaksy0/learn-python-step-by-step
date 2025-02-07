import turtle
import time
def draw_spiral():
    t=turtle.Turtle()
    t.speed(0)
    for i in range(100):
        t.forward(i*5)
        t.right(144)
        time.sleep(0.1)
    turtle.done()
    
draw_spiral()        