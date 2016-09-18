import turtle


def drawFrac(lvl, s, up = True):
    if (lvl == 0):
        turtle.forward(s)
        return

    drawFrac(lvl - 1, s / 3, up)
    if (up):
        turtle.left(60)
    else:
        turtle.right(60)
    
    drawFrac(lvl - 1, s / 3, up)

    if (up):
        turtle.right(120)
    else:
        turtle.left(120)
        
    drawFrac(lvl - 1, s / 3, up)

    if (up):
        turtle.left(60)
    else:
        turtle.right(60)

    drawFrac(lvl - 1, s / 3, up)


def main():
    turtle.title("Fractal madness")
    turtle.speed("fastest")
    s = 800
    lvl = 3
    
    turtle.penup()
    turtle.back(s / 2)
    turtle.pendown()

    p = turtle.pos()
    drawFrac(lvl, s)

    '''turtle.penup()
    turtle.setpos(p)
    turtle.pendown()
    
    drawFrac(lvl, s, False)'''
    
    turtle.exitonclick()

main()
