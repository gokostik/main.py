from turtle import *
import random

import timer

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

screen.bgcolor(100,100,100)
textout = Turtle()
textout.up()
textout.setpos(-1980/2+50, 1050/2-20)
textout.write("Q - Heart    W - Flour   ] - Quit", font=("Arial", 16, "normal"))

move = Turtle()

def showpos():
    global move, movespeed
    textout.up()
    textout.setpos(-1980 / 2 + 50, 1050 / 2 - 105)
    textout.down()
    textout.pencolor(100, 100, 100)
    textout.write("████████████████████████████████████████", font=("Arial", 24, "normal"))
    textout.pencolor(0, 0, 0)
    textout.write(f"{move.pos()} speed {movespeed}", font=("Arial", 24, "normal"))
    ontimer(showpos, 900)

def tocenter():
    move.setpos(0, 0)

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

def kvadrat1():
    move.down()
    move.forward(150)
    move.right(90)
    move.forward(150)
    move.right(90)
    move.forward(150)
    move.right(90)
    move.forward(150)
    move.up()

def speedup():
    global movespeed
    movespeed = movespeed+1
    move.speed(movespeed)

def speeddown():
    global movespeed
    movespeed = movespeed-1
    move.speed(movespeed)

def k0():
    quit()

def k1():
    move.forward(5)

def k2():
    move.left(5)

def k3():
    move.right(5)

def k4():
    move.back(5)

def k5():
    move.down()
    move.left(45)
    move.forward(105)
    move.circle(50,200)
    move.right(125)
    move.circle(50,200)
    move.forward(105)
    move.up()

def k6():
    global gogogo, n
    gogogo=True
    move.speed(0)
    if n >= 1000:
        n=0


    while (n < 1000) and (gogogo):
        listen()
        textout.up()
        textout.setpos(-1980 / 2 + 50, 1050 / 2 - 70)
        textout.down()
        textout.pencolor(100,100,100)
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
#    move.write(str(x) + "," + str(y))
    showpos()


screen.onclick(fxn)
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
onkeypress(kvadrat1, "d")
onkeypress(tocenter, "z")
onkeypress(showpos, "p")
onkeypress(screen.reset, "/")
ontimer(showpos, 50)

listen()
mainloop()