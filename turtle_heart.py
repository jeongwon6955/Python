import turtle as t
t.bgcolor('black')
t.pensize(5)

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.speed(1)
t.color('red', 'pink')

t.begin_fill()
t.left(140)
t.forward(111)
curve()

t.left(120)
curve();
t.forward(111)
t.end_fill()
t.hideturtle()

t.done()