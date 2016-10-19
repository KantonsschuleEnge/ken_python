import numpy as np
from quaternions import *



datei = open('vektoren.txt','r')
erg = open('erg.txt','w')
vektoren = []
for line in datei:
    v=[]
    for koord in line.split():
        v.append(float(koord))
    vektoren.append(v)
print(vektoren)
erg.write(str(vektoren))

q1 = fillpositive([0.25,-0.5,0.1])
q2 = fillpositive([-0.25,-0.5,0.1])
print(q1)
print(conjugate(q1))
print(norm(q1))

neuePunkte=[]
for p in vektoren:
    neuePunkte.append(rotate_vector(p,q1))
print(neuePunkte)
erg.write(str(neuePunkte))
datei.close()
erg.close()
input()
