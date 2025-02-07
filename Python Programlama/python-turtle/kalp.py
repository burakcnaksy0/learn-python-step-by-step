import turtle

def draw_heart():
    t=turtle.Turtle()
    t.begin_fill()
    t.fillcolor("red")
    t.left(50)
    t.forward(133)
    t.circle(50,200)
    t.right(140)
    t.circle(50,200)
    t.forward(133)
    t.end_fill()
    turtle.done()

draw_heart()    