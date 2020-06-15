import numpy as np


def umwandlung(liste):
    ausgabeliste = []
    for i in range(len(liste)):
        if liste[i]%2 != 0:
            ausgabeliste.append(liste[i])

    return ausgabeliste


x = []
for step in range(1, 100):
    x.append(np.random.randint(1, 100))


print("Ursprüngliche Listenlänge:",len(x))

um = umwandlung(x)
print(um)
print("Listeeinträge nach kürzung:",len(um))