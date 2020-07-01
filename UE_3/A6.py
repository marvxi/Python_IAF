import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,np.pi/30)
y = lambda x:np.sin(x)**2

#-----Plots--------
#Subplot1 A6 a)
plt.subplot(4,1,1)
plt.plot(x,y(x),'y-3',label="Beide Achsen linear")
plt.ylabel("y")
plt.grid()
plt.legend(loc="lower right")

plt.subplot(4,1,2)
plt.semilogy(x,y(x),'b-4',label="y-Achse logarithmisch")
plt.ylabel("y")
plt.grid()
plt.legend()

plt.subplot(4,1,3)
plt.semilogx(x,y(x),'r-4',label="x-Achse logarithmisch")
plt.ylabel("y")
plt.grid()
plt.legend(loc='lower right')

plt.subplot(4,1,4)
plt.loglog(x,y(x),'g-3',label="Beide Achsen logarithmisch")
plt.ylabel("y")
plt.xlabel("x")
plt.grid()
plt.legend(loc='lower right')

plt.show()