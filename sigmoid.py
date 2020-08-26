import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,1,10)

def func(x):
    return 1/(1+np.exp(-x))
def derivfunc(x):
    return (1/(1+np.exp(-x))) * (1-1/(1+np.exp(-x)))

plt.figure(dpi=200)
plt.plot(x,func(x),label='Sigmoidfunktion')
plt.plot(x,derivfunc(x),'r--',label='Ableitung der Sigmoidfunktion')
plt.xlabel('x-Werte')
plt.ylabel('y-Werte')
plt.grid()
plt.legend()
plt.show()