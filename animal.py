import turtle
from turtle import *
import time
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(16):
    write(step, align= 'center')
    right(90)
    forward(10)
    pendown()
    forward(300)
    penup()
    backward(310)
    left(90)
    forward(20)

ada = Turtle()
ada.color('blue')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('red')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

cal = Turtle()
cal.color('yellow')
cal.shape('turtle')

cal.penup()
cal.goto(-160, 40)
cal.pendown()

dex = Turtle()
dex.color('black')
dex.shape('turtle')

dex.penup()
dex.goto(-160, 10)
dex.pendown()

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    cal.forward(randint(1,5))
    dex.forward(randint(1,5))



turtle.done()

