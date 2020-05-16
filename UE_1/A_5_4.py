import numpy as np
number = int(input("Gib eine beliebige Zahl ein: "))

zahl_m = 0
zahl_o = 100
random = np.random.uniform(zahl_m,zahl_o)
x = int(np.ceil(random))

#x = 32
count = 0
while number != x:
    count +=1
    if number > x:
        print("Deine Zahl ist zu Groß!")
    elif number < x:
        print("Deine Zahl ist zu klein!")

    number = int(input("Gib erneut eine Zahl ein: "))

print(f'Spiel gewonnen mit {count} versuchen.')