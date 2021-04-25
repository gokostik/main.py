from turtle import *
import random

is_draw = True
gogogo = True
movespeed = 1
n = 0

timy = Turtle()
timy.shape("arrow")
timy.hideturtle()
colormode(255)
timy.pencolor(222,123,255)
timy.pensize(1)
timy.shapesize(2)
timy.speed(3)

screen = Screen()

  #set size:

screen.setup(width = 1.0, height = 1.0)

#remove close,minimaze,maximaze buttons:
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

textout = Turtle()
textout.up()
textout.setpos(-1980/2+50, 1050/2-20)
textout.write("Q - Heart    W - Flour   ] - Quit", font=("Arial", 16, "normal"))

move = Turtle()

def showpos():
    textout.up()
    textout.setpos(-1980 / 2 + 50, 1050 / 2 - 105)
    textout.down()
    textout.pencolor(255, 255, 255)
    textout.write("███████████████████████████████", font=("Arial", 24, "normal"))
    textout.pencolor(0, 0, 0)
    textout.write(f"{move.pos()} speed {movespeed}", font=("Arial", 24, "normal"))

def tocenter():
    move.setpos(0, 0)
    showpos()

def kvadrat():
    move.down()
    move.forward(150)
    move.left(90)
    move.forward(150)
    move.left(90)
    move.forward(150)
    move.left(90)
    move.forward(150)
    move.up()
    showpos()

def speedup():
    global movespeed
    movespeed = movespeed+1
    move.speed(movespeed)
    showpos()

def speeddown():
    global movespeed
    movespeed = movespeed-1
    move.speed(movespeed)
    showpos()

def k0():
    quit()

def k1():
    move.forward(5)
    showpos()

def k2():
    move.left(5)
    showpos()

def k3():
    move.right(5)
    showpos()

def k4():
    move.back(5)
    showpos()

def k5():
    move.down()
    move.left(45)
    move.forward(105)
    move.circle(50,200)
    move.right(125)
    move.circle(50,200)
    move.forward(105)
    move.up()
    showpos()

def k6():
    global gogogo, n
    gogogo=True
    move.speed(0)
    if n >= 1000:
        n=0


    while (n < 1000) and (gogogo):
        listen()
        showpos()
        textout.up()
        textout.setpos(-1980 / 2 + 50, 1050 / 2 - 70)
        textout.down()
        textout.pencolor(255,255,255)
        textout.write( "██████ [get some bread]", font=("Arial", 24, "normal"))
        textout.pencolor(0,0,0)
        textout.write(n, font=("Arial", 24, "normal"))
        move.down()
        move.circle(50, 201)
        move.right(129)
        move.circle(50, 201)
        move.right(129)
        move.circle(50, 201)
        move.right(129)
        move.circle(50, 201)
        move.right(129)
        move.circle(50, 201)
        move.up()
        n=n+1

def k7():
    global is_draw
    if is_draw:
        move.up()
    else:
        move.down()
    is_draw = not is_draw


def k00():
    global gogogo
    gogogo=False

def fxn(x, y):
    move.goto(x, y)
    showpos()

onclick(fxn)
onkeypress(k0, "]")
onkeypress(k00, "[")
onkeypress(speedup, ".")
onkeypress(speeddown, ",")
onkeypress(k1, "Up")
onkeypress(k2, "Left")
onkeypress(k3, "Right")
onkeypress(k4, "Down")
onkeypress(k5, "q")
onkeypress(k6, "w")
onkeypress(k7, "space")
onkeypress(kvadrat, "s")
onkeypress(tocenter, "z")
onkeypress(showpos, "p")
onkeypress(screen.reset, "/")





listen()
mainloop()

while True:
    timy.begin_fill()
    timy.left(45)
    timy.forward(105)
    timy.circle(50,200)
    timy.right(125)
    timy.circle(50,200)
    timy.forward(105)
    timy.up()

    timy.forward(200)
    timy.down()

    timy.circle(50, 201)
    timy.right(129)
    timy.circle(50, 201)
    timy.right(129)
    timy.circle(50, 201)
    timy.right(129)
    timy.circle(50, 201)
    timy.right(129)
    timy.circle(50, 201)

    timy.up()

    timy.forward(200)
    timy.down()