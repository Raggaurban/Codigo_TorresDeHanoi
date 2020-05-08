import turtle as t

t.setup(500,500)

t.shape("turtle")
t.color("blue")

def poligono_regular(px, py, radio, lados):
    t.penup()

    angulo = 360 / lados
    print(angulo)

    vertices = []

    for i in range(lados):
        t.goto(px, py)

        t.seth(angulo*i+1)
        t.forward(radio)
        vertices.append(t.pos())

    t.goto(vertices[-1])
    t.pendown()

    for v in vertices:
        t.goto(v)

t.speed(200)
for n in range(3, 21):
    poligono_regular(0, 0, n*10, n)

t.done()
t.bye()
