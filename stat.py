from turtle import *

def balken(h):
    for i in range(2):
        fd(h)
        rt(90)
        fd(20)
        rt(90)

def statistik(dict):
    for key in dict:
        rt(90)
        pu()
        fd(40)
        pd()
        lt(90)
        balken(dict[key])
        write(key)

stat={'a':100,'b':200,'c':175}

statistik(stat)
