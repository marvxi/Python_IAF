import matplotlib.pyplot as plt
import numpy as np

def MyFunction(x):  # Diese Funktion ist eine "echte" Funktion
    return x**2+3*x+5

y = lambda x: x**2+4*x+5

#x-Wertebereich
x = np.linspace(-10,10,100) #Start und Endwert und wie viele Werte

#MyFunction = x**2+3*x+5
plt.plot(x,MyFunction(x),label="Polynom")
plt.plot(x,y(x),label="Polynom Lambda")


plt.xlabel("x-achse") #Mindesanforderung für Plot!!! Wichtig
plt.ylabel("y-achse")
plt.legend()
plt.grid()
plt.show()