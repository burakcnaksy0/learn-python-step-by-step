#python'da turtle nedir ?
#turtle grafikler ve basit cizimler yapmak icin kullanilan bir moduldur
#turtle kendi icerisindeki komutlar sayesinde grafigimizi tasarlamımıza saglar
#sag sol ileri ve geri gidebilecegim komutlar sayesinde istedigimiz sekli
#animasyonu yapmamızı saglayan bir moduldur

#ornek1 Daire Grafigi Cizelim
import turtle

def draw_circle():
    t=turtle.Turtle()
    t.circle(100)
    turtle.done()

draw_circle()    