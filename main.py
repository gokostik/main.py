from turtle import *
import random


is_draw = True
is_show_coordinates = False
go_go_go = True
move_speed = 1
pen_size = 1
n = 0


timy = Turtle()
timy.shape("arrow")
timy.hideturtle()
colormode(255)
timy.pencolor(222, 123, 255)
timy.pensize(1)
timy.shapesize(2)
timy.speed(3)
screen = Screen()
screen.setup(width=1.0, height=1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
screen.bgcolor(100, 100, 100)
textout = Turtle()
textout.up()
textout.setpos(-1980/2+50, 1050/2-20)
textout.write("[Пробіл]Викл/вкл ручку [Q]Сердце [W]Квітка [S]Квадрат [E]Зірка [I]Показати координати []]Вихід",
              font=("Arial", 16, "normal"))
move = Turtle()


def star():
    speed(0)
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(900)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()


def set_pen_size(size):
    global pen_size
    pen_size = size
    move.pensize(size)


def showpos():
    global move, move_speed
    textout.up()
    textout.setpos(-1980 / 2 + 50, 1050 / 2 - 105)
    textout.down()
    textout.pencolor(100, 100, 100)
    textout.write("█████████████████████████████████████████████████", font=("Arial", 16, "normal"))
    textout.pencolor(0, 0, 0)
    if move.isdown():
        my_text = "Фарба ВКЛ"
    else:
        my_text = "Фарба ВИКЛ"
    textout.write(f"Кут [{move.heading()}]p Координати [{move.pos()}] [Швидкість={move_speed}] [Товщина={pen_size}] [{my_text}]", font=("Arial", 16, "normal"))
    ontimer(showpos, 1000)


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
    global move_speed
    move_speed = move_speed + 1
    move.speed(move_speed)


def speeddown():
    global move_speed
    move_speed = move_speed - 1
    move.speed(move_speed)


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
    move.circle(50, 200)
    move.right(125)
    move.circle(50, 200)
    move.forward(105)
    move.up()


def k6():
    global go_go_go, n
    go_go_go = True
    move.speed(0)
    if n >= 1000:
        n = 0
    while n < 1000 and go_go_go:
        listen()
        textout.up()
        textout.setpos(-1980 / 2 + 50, 1050 / 2 - 70)
        textout.down()
        textout.pencolor(100, 100, 100)
        textout.write("█████████", font=("Arial", 24, "normal"))
        textout.pencolor(0, 0, 0)
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
        n = n+1


def k7():
    global is_draw
    if is_draw:
        move.up()
    else:
        move.down()
    is_draw = not is_draw


def k00():
    global go_go_go
    go_go_go = False


def coordinates():
    global is_show_coordinates
    is_show_coordinates = not is_show_coordinates


def fxn(x, y):
    move.goto(x, y)
    if is_show_coordinates:
        move.write(str(x) + "," + str(y))



def pen1():
    set_pen_size(1)


def pen2():
    set_pen_size(2)


def pen3():
    set_pen_size(3)


def pen4():
    set_pen_size(4)


def pen5():
    set_pen_size(5)


def pen6():
    set_pen_size(6)


def pen7():
    set_pen_size(7)


def pen8():
    set_pen_size(8)


def pen9():
    set_pen_size(9)


def pen10():
    set_pen_size(10)


def pen_plus():
    global pen_size
    pen_size += 1
    move.pensize(pen_size)


def pen_minus():
    global pen_size
    pen_size -= 1
    move.pensize(pen_size)


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
onkeypress(coordinates, "i")
onkeypress(kvadrat, "s")
onkeypress(kvadrat1, "d")
onkeypress(tocenter, "z")
onkeypress(showpos, "p")
onkeypress(screen.reset, "/")
onkeypress(star, "e")


onkeypress(pen1, "1")
onkeypress(pen2, "2")
onkeypress(pen3, "3")
onkeypress(pen4, "4")
onkeypress(pen5, "6")
onkeypress(pen6, "6")
onkeypress(pen7, "7")
onkeypress(pen8, "8")
onkeypress(pen9, "9")
onkeypress(pen10, "0")
onkeypress(pen_plus, "+")
onkeypress(pen_minus, "-")

ontimer(showpos, 50)
listen()
mainloop()
