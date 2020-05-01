from math import *
import matplotlib.pyplot as plt

def LogAbfrage():
    #x = float(input('x='))
    x = 0
    xValue=[]
    yValue=[]

    while x <= 3*pi:

        if 0<= x <= pi:
            val = sin(x)

        elif pi < x <=2*pi:
            val = -sin(x)

        elif 2*pi < x <= 3*pi:
            val = sin(x)

        else:
            val = 0.0


        xValue.append(x)
        yValue.append(val)
        x += pi / 50

    print(' x=%-8g val=%-8g' %(x,val))
    print(xValue)
    print(yValue)
    fig = plt.figure(1,figsize=(6,4))
    plt.plot(xValue,yValue)
    plt.xlabel('x');
    plt.ylabel('y')
    plt.title('Sinus Plot')
    plt.show()

LogAbfrage()

