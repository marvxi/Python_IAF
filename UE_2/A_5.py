import numpy as np
x = []
for step in range(1, 100):
    x.append(np.random.randint(1, 100))

def delete(zahl,liste):
    for i in range(liste.count(zahl)):
        liste.remove(zahl)

    return liste

print(x)
zahl = int(input("Gebe die zu löschende Zahl ein:"))

print(delete(zahl,x))
