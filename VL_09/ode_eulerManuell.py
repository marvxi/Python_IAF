# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:08:27 2019

@author: pscholle
"""

import numpy as np
import matplotlib.pyplot as plt

# Beispiel 1 ##################################################################

#step = 0.5 # h
#t1 = np.arange(0,5,0.02) # Feiner Zeitvektor
#t2 = np.arange(0,5,step) # Grober Zeitvektor mit h=step
#
#y1 = 2.5*t1**2 # analytical solution
#y2 = np.zeros(len(t2))
#
#for i in range(1,len(t2)):
#    y2[i] = y2[i-1] + step*5*t2[i-1]
#
#plt.figure(1)
#plt.plot(t1,y1,label='analytical')
#plt.plot(t2,y2,'o-',label='numeric explicit')
#
#plt.legend()
#
#from scipy.integrate import solve_ivp
#
#def func(t,y):
#    yp = 5*t+y*0
#    return yp
#    
#sol = solve_ivp(func,t_span=(0,5),y0=[0])
#plt.plot(sol.t,sol.y[0,:],'o-',label='solve_ivp')
#plt.legend()


# steife ODE ##################################################################

# Euler explizit
step = 0.1 # h
t1 = np.arange(0,5,0.02) # Feiner Zeitvektor
t2 = np.arange(0,5,step) # Grober Zeitvektor mit h=step

y1 = 2-np.exp(-5*t1) # analytical solution
y2 = np.ones(len(t2))
for i in range(0,len(t2)-1):
    y2[i+1] = y2[i] + step*(-5*(y2[i]-2))
	
plt.figure(2)
plt.plot(t1, y1, label='analytical')
plt.plot(t2, y2, 'o-', label='numeric explicit')

plt.legend()

# Euler implizit
step = 0.5
t3 = np.arange(0, 5, step)
y3 = np.ones(len(t3))
for i in range(0, len(t3)-1):
    y3[i+1] = (y3[i]+10*step) / (1+5*step)
plt.plot(t3, y3, 'o-', label='numerical implicit')
plt.legend()
#
#
# scipy integrate solver
from scipy.integrate import solve_ivp

def func(t,y):
    yp = -5*(y-2)
    return yp
    
sol = solve_ivp(func,t_span=(0,5),y0=[1])
plt.plot(sol.t,sol.y[0,:],'o-',label='solve_ivp')
plt.legend()