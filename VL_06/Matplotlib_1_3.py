import matplotlib.pyplot as plt
import numpy as np

plt.figure()


x = np.linspace(0,2,100)
y = np.exp(x)

plt.subplot(2,2,1)
plt.plot(x,y,label="$e^x$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

x = np.linspace(0,4,100)
plt.subplot(2,2,2)
plt.semilogx(x,y,label="$Semilogxe^x$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

x = np.linspace(0,7,100)
plt.subplot(2,2,3)
plt.semilogy(x,y,label="$semilogye^x$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()


plt.subplot(2,2,4)
plt.loglog(x,y,label="$logloge^x$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()