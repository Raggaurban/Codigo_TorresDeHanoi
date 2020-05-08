import turtle as t

t.setup(500,500)
t.pensize(5)

t.shape("turtle")
t.color("red")

def rectangulo(px, py, ancho, alto):
    t.penup()
    t.goto(px + ancho / 2, py + alto / 2)
    t.seth(180)
    t.pendown()

    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)

rectangulo(0, 0, 400, 300)
rectangulo(0, 0, 300, 200)
rectangulo(0, 0, 200, 100)
rectangulo(0, 0, 50, 50)

t.done()
t.bye()
