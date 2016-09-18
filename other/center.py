import turtle

t = turtle
t.speed("fastest")

def triangle(s):
    t.forward(s)
    t.left(120)
    t.forward(s)
    t.left(120)
    t.forward(s)

def square(s):
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.forward(s)
    t.left(90)
    t.forward(s)

def boorick():
    for i in range(1, 800, 5):
        #triangle(i)
        square(i)
        t.circle(i)
        t.setheading(i)

boorick()
t.exitonclick()
