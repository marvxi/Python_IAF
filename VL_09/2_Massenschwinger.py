import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#Konstanten
#Dämpfer
b1 = 15
b2 = 5
#Feder
c1 = 40
c2 = 10
#Masse
m1 = 2
m2 = 10
#AB
y0 = [1,0,-1,0] # Anfangsauslenkung für x1 = 1, Anfangsgeschgeschwindigkeit x1 = 0, Auslenkung x2 = -1, Geschw. x2 = 0
t = (0,40)

def func2Massen(t,y):
    dy1 = y[1]
    dy2 = -10*y[1]+2.5*y[3]-25*y[0]+5*y[2]+np.sin(3*t)
    dy3 = y[3]
    dy4 = 0.5*y[1]-0.5*y[3]+y[0]-y[2]+0.5*np.cos(5*t)
    return [dy1,dy2,dy3,dy4]

solve2Massen = solve_ivp(func2Massen,t,y0,max_step=0.1)

plt.figure()
plt.plot(solve2Massen.t,solve2Massen.y[0],label="m1")
plt.plot(solve2Massen.t,solve2Massen.y[2],label="m2")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()