import numpy as np
import matplotlib.pyplot as plt

# Explizit
h1 = 0.1
t1 = np.arange(0,5,0.02)
t2 = np.arange(0,5,h1)

y1 = 2-np.exp(-5*t1) # analytical solution

#Achtung bei großen Schrittweiten wird die Lösung instabil, verkleinere Schrittweite. Nur bei Expliziten Verfahren ein Problemen
y=np.ones(len(t2))
for i in range(0,len(t2)-1):
    y[i+1] = y[i] + h1*(-5*(y[i]-2))

plt.figure()
plt.plot(t1,y1,label='Analytische Lösung')
plt.plot(t2,y,label="Explizite Verfahren")
plt.ylabel("y")
plt.xlabel("t")

#Implizit
h = 0.1
t3 = np.arange(0,5,h)
y3 = np.ones(len(t3))
for i in np.arange(0,len(t3)-1):
    y3[i+1] = (y[i]+10*h)/(1+5*h)

plt.plot(t3,y3,'o-',label="Implizite Verfahren")


#---- scipy.integrate.solve_ivp
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def func(t,y):
    dy = -5*(y-2)
    return dy

solution = solve_ivp(func,t_span=(0,5),y0=[1]) #Übergeben werden müssen, funktion, Zeitbereich und Anfangswert
plt.plot(solution.t, solution.y[0],'o-',label="solve_ivp") #Achtung y ist ein arry und es muss der 0 Eintrag genommen werden
plt.legend()
plt.grid()
plt.show()
