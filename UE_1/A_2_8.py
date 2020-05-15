from math import pi

x = input('Gib den Druchmesser des Kreises an: ')
x = float(x)

print('Umfang des Kreises: ',x * pi )
x = x/2
print('Fläche des Kreises: ', x**2 * pi)