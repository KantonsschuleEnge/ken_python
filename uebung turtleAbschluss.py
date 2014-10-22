#!/urs/bin/python3
# gregor Luedi
# Loesungen Uebungen Python Turtle


from turtle import *

#Aufgabe 1
def Aufgabe1():
    name = input('Geben Sie ihren Namen ein:')

    for i in range(50):
        print('Hallo ',name)

#Aufgabe 2
def Rechteck(laenge,breite):
    for i in range(2):
        for s in [laenge,breite]:
            fd(s)
            rt(90)


#Aufgabe 3
def Stern(seite):
    for i in range(6):
        fd(seite)
        rt(120)
        fd(seite)
        lt(60)

#Aufgabe 4


def Umrechnung():
    c = float(input('Geben Sie die Temperatur in Celsius ein:'))
    f = 1.8*c+32
    print('Die Temperatur {}° in Celsius entspricht einer Temperatur von {}° Fahrenheit.'.format(c,f))


Umrechnung()
