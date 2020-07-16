from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
alpha = 1
beta = -1
gamma = 0.3
delta = 0.2
Omega1 = 1.3
Omega2 = 1.4
x0 = [0,0]
def func_duffing(t,y):
    y1p = y[1]
    #y2p = gamma*np.cos(Omega1*t)-delta*y[1]-beta*y[0]-alpha*y[0]**3
    y2p = -delta*y[1] - beta*y[0] - alpha*y[0]**3 + gamma*np.cos(Omega1*t)
    return [y1p,y2p]
t=(0,150)
solution = solve_ivp(func_duffing,t,x0)
plt.figure(1)
plt.subplot(211)
plt.plot(solution.t,solution.y[0,:])
plt.xlabel('Zeit')
plt.ylabel('Weg')
plt.subplot(212)
plt.plot(solution.y[0],solution.y[1])
plt.xlabel('Weg')
plt.ylabel('Geschwindigkeit')
plt.tight_layout()
plt.show()