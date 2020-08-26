import numpy as np
import matplotlib.pyplot as plt

# Schrittweite
h = np.array([3.0,1.5,0.1,0.01,0.001])

# x Werte
x = np.linspace(0,10,5)

# Funktion
def func(x):
    return -2*x**2+3*x - 40
# Ableitung der Funktion
def deriv(x):
    return -4*x+3
# Taylorreihe
def taylor(x0,h=h):
    return (func(x0+h)-func(x0))/h

x0=5
#print(f'Funktion: {func(x0)}')
#print(f'Ableitung: {deriv(x0)}')
#print(f'Approx.: {taylor(x0,h)}')
#
## Fehler zwischen approx. und tatsächlicher lösung
#print(f'Error {taylor(x0,h) - deriv(x0)}')

#Plots

plt.loglog(h,deriv(x0) - taylor(x0,h),'r-o',label="Error")
plt.xlabel('Schrittweite h')
plt.ylabel('Error')
plt.grid()
plt.legend()
plt.show()
