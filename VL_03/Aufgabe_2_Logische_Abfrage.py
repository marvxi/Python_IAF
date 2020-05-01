from math import *
import matplotlib.pyplot as plt

x = 0
xValue = []
yValue = []

while x <= 2*pi:
    xValue.append(x)

    if x == 0:
        yValue.append(cos(x))

    else:
        yValue.append(sin(x)/x)

    x+=2.*pi/100

fig = plt.figure(1,figsize=(6,4))
plt.plot(xValue,yValue)
plt.xlabel('x');
plt.ylabel('y')
plt.title('Sin(x)/x')
plt.show()