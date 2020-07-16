import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

st = 0 # Startzeit
et = 5 # Endzeit
ts = 0.01 #Time step(s)
g = 9.81 # Gravity (m/s^2)
L = 1 # Lenght of pendulum (m)
T = (st,et) #Tupel

# System von zwei Differentialglichungen 1. Ordnung
def func_linpendel(t,phi):
    dphi1 = phi[1]
    dphi2 = (-g/L)*phi[0]
    return [dphi1,dphi2]
# Nicht lineares System

def func_nonlinpedel(t,phi):
    dphi1 = phi[1]
    dphi2 = (-g/L)*np.sin(phi[0])
    return [dphi1,dphi2]

#Anfangsbedingungen
phi0 = [1,2] # Warum, 1 Eintrag ist Winkel 2 ist Winkelbeschleunigung
t = (st,et)


sol_lin = solve_ivp(func_linpendel,t,phi0,method="RK45",max_step=ts)
sol_nlin = solve_ivp(func_nonlinpedel,t,phi0,method="RK45",max_step=ts)

plt.figure()
plt.plot(sol_lin.t,sol_lin.y[0,:],label="linear")
plt.plot(sol_nlin.t,sol_nlin.y[0,:],label="nicht linear")
plt.legend()
plt.grid()
plt.show()
