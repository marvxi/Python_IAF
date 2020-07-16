# scipy.integrate.solve_ivp
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

'''
dy1 = -80.59*y1 + 119.4*y2
dy2 = 79.6*y1 - 120.4*y2
dy1(0) = 0, dy2(0) = 1
'''
def func(t,y):
    dy1 = -80.59 * y[0] + 119.4 * y[1]
    dy2 = 79.6 * y[0] - 120.4 * y[1]
    return [dy1,dy2]

sol45 = solve_ivp(func,t_span=(0,10),y0=[0,1],method='RK45')
plt.figure()
plt.subplot(121)
plt.title("RK45")
plt.plot(sol45.t,sol45.y[0,:],'o-',label="y1") #Achtung y[0,:] sind die unterschiedlichen Lösungsvektoren
plt.legend()
plt.grid()
plt.subplot(122)
plt.plot(sol45.t,sol45.y[1,:],'o-',label="y2")
plt.legend()
plt.grid()
plt.show()