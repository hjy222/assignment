import turtle
import random
import time

def Wind(x,y):
    time.sleep(0.001)
    t.color("white")
    t.penup()
    t.goto(x,y)
    t.begin_fill()
    t.setheading(90)
    t.circle(-8, 180)
    t.setheading(90)
    t.circle(-16, 180)
    t.setheading(90)
    t.circle(-8, 180)
    t.setheading(0)
    t.circle(-16, 180)
    t.setheading(-90)
    t.circle(-8, 180)
    t.setheading(-90)
    t.circle(-16, 180)
    t.setheading(-90)
    t.circle(-8, 180)
    t.setheading(0)
    t.circle(16, -150)
    t.setheading(90)
    t.end_fill()


def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('lightpink')
            else:
                t.color('lightcoral')
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('lightpink')
            else:
                t.color('lightcoral')
            t.pensize(branch / 2)
        else:
            t.color('sienna')
            t.pensize(branch / 10)
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

# 掉落的花瓣
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        if random.randint(0, 2) == 0:
            t.color('lightpink')
        else:
            t.color('lightcoral')
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


t = turtle.Turtle()
w = turtle.Screen()
t.hideturtle()
t.getscreen().tracer(5, 0)
w.screensize(bg='lightcyan')
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')


Tree(60, t)
Petal(100, t)
Wind(-200,270)
Wind(-50,300)
Wind(60,260)
Wind(180,280)
w.exitonclick()
turtle.done()
