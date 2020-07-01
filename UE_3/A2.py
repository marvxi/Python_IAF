import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,10,0.001)
omega = 1.0

def func1(t,omega):
    return 4/(np.pi) * np.sin(omega*t) + 4/(3*np.pi) * np.sin(3*omega*t)

def func2(t,omega):
    return 4/(np.pi) * np.sin(omega*t) + 4/(3*np.pi) * np.sin(3*omega*t) + 4/(5*np.pi) * np.sin(5*omega*t) + 4/(7*np.pi) * np.sin(7*omega*t) + 4/(9 * np.pi) * np.sin(9 * omega * t)

#plot

plt.plot(t,func1(t,omega),label="Funktion1")
plt.plot(t,func2(t,omega),label="Funktion2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()