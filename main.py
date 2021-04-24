from turtle import *
import random

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

move = Turtle()

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

def k7():
    move.down()

onkeypress(k1, "Up")
onkeypress(k2, "Left")
onkeypress(k3, "Right")
onkeypress(k4, "Down")
onkeypress(k5, "q")
onkeypress(k6, "w")
onkeypress(k7, "space")

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


    # # timy.forward(random.randint(100, 150))
    # #
    # timy.down()
    # x = random.randint(1, 150)
    # timy.left(120)
    # timy.forward(x)
    # timy.pencolor((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
    #
    # timy.left(120)
    # timy.forward(x)
    # timy.pencolor((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
    #
    # timy.left(120)
    # timy.forward(x)
    # timy.pencolor((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
    #
    # timy.right(90)
    # timy.forward(x)
    # timy.pencolor((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
    #
    # timy.right(90)
    # timy.forward(x)
    # timy.pencolor((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
    #
    # timy.right(90)
    # timy.forward(x)
    # timy.pencolor((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
    #
    # timy.right(90)
    # timy.forward(x)
    # timy.pencolor((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))\
    #
    # timy.up()
    # timy.left(random.randint(0, 30))
    # timy.left(random.randint(0,360))
    #
    #
    # timy.forward(random.randint(0, 150))
    # timy.pencolor((random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)))
    # timy.pensize(random.randint(20,50))
    #
    # timy.down()
    # timy.circle(random.randint(0,150))
    # timy.right(random.randint(0, 360))
    # timy.speed(random.randint(1, 10))
    # timy.pencolor((random.randint(100, 255),random.randint(100, 255),random.randint(100, 255)))
    # timy.pensize(random.randint(20, 50))
    # timy.up()

