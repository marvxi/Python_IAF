import numpy as np
import matplotlib.pyplot as plt

# Schrittweite
h = 0.5
# Schallgeschwindigkeit
c = 343.2

# Schrittweite
h = 0.2

# Startwert Zeit
dt = 0.1

#Länge
width = 10

# Anzahl der Schritte in 1D Richtung
nx = int(width/h)

x = np.linspace(0,width,nx)

X = np.meshgrid(x)

# Zeitdauer
t = 2

# steifikeit
k = 1

# AB
u = np.zeros((nx))
u0 = 2 * np.ones((nx))

for time in np.linspace(0,t,int(t/dt)):
    for i in range(1,len(x) - 1):

        u[i] = (c*((u[i+1] - 2*[i] + u[i-1])/h**2) + 2*u[i]*(1 + k * dt) - u[i]) / (1+2*k*dt)