#Spiel für 1 Spieler
import numpy as np
Punkte = int(0)

while Punkte < 100:

    for i in range(5):
        würfel = 0
        help = 0
        würfel = int(np.random.uniform(1, 6))
        print(würfel)
        help += würfel
        if würfel == 1:
            help = 0
            break

    Punkte += help
    if Punkte > 100:
        Punkte -= help

    print(Punkte)
