import numpy as np
import matplotlib.pyplot as plt

#const
n = np.arange(0,5,0.001)

def VergrFun(n,D):
    return 1/(np.sqrt((1-n**2)**2+(2*D*n)**2))

plt.figure(1)
plt.semilogy(n,VergrFun(n,0.01),label="D=0.0")
plt.semilogy(n,VergrFun(n,0.05),label="D=0.2")
plt.semilogy(n,VergrFun(n,0.1),label="D=0.4")
plt.semilogy(n,VergrFun(n,0.2),label="D=0.6")
plt.semilogy(n,VergrFun(n,0.5),label="D=0.8")
plt.semilogy(n,VergrFun(n,1.0),label="D=1.0")
plt.title("Vergrößerungsfunktionen mit verschiedenen Dämpfungen")
plt.ylabel("V")
plt.xlabel("n")
plt.legend()
plt.grid()

plt.show()

D=np.append([0.01, 0.05], np.arange(0.1,1.1,0.1))
print(D)