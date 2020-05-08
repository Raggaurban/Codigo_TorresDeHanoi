import turtle as t

t.setup(500, 500)
t.pensize(3)

t.shape("turtle")
t.color("purple")

def derecha():
    t.seth(0)
    t.forward(20)


def izquierda():
    t.seth(180)
    t.forward(20)


def arriba():
    t.seth(90)
    t.forward(20)


def abajo():
    t.seth(270)
    t.forward(20)


def salir():
    t.bye()

t.onkey(arriba, "w")
t.onkey(izquierda, "a")
t.onkey(derecha, "d")
t.onkey(abajo, "s")
t.onkey(salir, "e")

t.listen()

t.done()
t.bye()