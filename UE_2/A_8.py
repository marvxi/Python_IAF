import numpy as np
liste = []

for i in range(50):
    liste.append(np.random.randint(0,10))
Tupel = tuple(liste)
zahl = int(input("Welche Zahl soll gezählt werden? "))
anz = Tupel.count(zahl)
print('Die Zahl {} kommt {} vor.'.format(zahl,anz))
