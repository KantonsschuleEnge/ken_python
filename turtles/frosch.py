from turtle import *
speed(0)

def quadrat(seite):
    for i in range(4):
        fd(seite)
        rt(90)

def quadratfett(seite):
    color('black','black')
    begin_fill()
    quadrat(seite)
    end_fill()

def frosch(h):
    pu(), fd(h*13), pd()
    rt(90)
    fd(h*21), rt(90), fd(h*2), lt(90), fd(h*2), rt(90), fd(h*9), rt(90), fd(h*2), lt(90), fd(h*2), rt(90), fd(h*9), rt(90), fd(h*2), rt(90), fd(h*7), bk(h*5), lt(90), fd(h*4), rt(90), fd(h*4), bk(h*4), lt(90), bk(h*2), lt(90), fd(h*5), lt(90), fd(h*4), rt(90), fd(h*7), rt(90), fd(h*2), rt(90), fd(h*5), lt(90), fd(h*4), lt(90), fd(h*7), rt(90), fd(h*7)

    rt(90), pu(), fd(h*2), rt(90), fd(h*2), lt(90), pd(), quadratfett(h*2), rt(90), pu(), fd(h*11), rt(90), fd(h*2), rt(90)

    rt(90), fd(h*30), lt(90)
    pd()

pu()
setpos(-200,0)
pd()
lt(90)
h = int(input('Froschgrösse eingeben: '))
nkinder = int(input('Anzahl Kinder eingeben: '))
frosch(h)
for i in range(nkinder):
    frosch(h/3)


