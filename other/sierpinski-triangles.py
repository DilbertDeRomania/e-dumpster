import turtle


MAXLEVEL = 5

def drawMainTriangle(size):
    turtle.pencolor("black")
    
    turtle.left(60)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(2 * size)
    turtle.right(120)
    turtle.forward(2 * size)
    turtle.right(120)
    turtle.forward(size)


def drawTriangleRec(level, size):
    turtle.pendown()
    turtle.setheading(0)

    if (level > MAXLEVEL or size < 5):
        return

    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.setheading(0)

    # draw left triangles
    p = turtle.pos()
    turtle.penup()
    turtle.right(120)
    turtle.forward(size / 2)
    
    drawTriangleRec(level + 1, size / 2)

    turtle.penup()
    turtle.setpos(p)
    turtle.pendown()

    #draw up triangle
    turtle.penup()
    turtle.left(60)
    turtle.forward(size / 2)

    drawTriangleRec(level + 1, size / 2)

    turtle.penup()
    turtle.setpos(p)
    turtle.pendown()

    #draw right triangle
    turtle.penup()
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size / 2)

    drawTriangleRec(level + 1, size / 2)

    turtle.penup()
    turtle.setpos(p)
    turtle.pendown()


def main():
    turtle.title("Sierpinski Triangles")
    turtle.speed("fastest")
    turtle.hideturtle()
    s = 300

    turtle.penup()
    turtle.forward(-150)
    turtle.pendown()
    
    drawTriangleRec(1, s)
    drawMainTriangle(s)
    turtle.exitonclick()

main()
