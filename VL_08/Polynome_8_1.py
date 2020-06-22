import numpy as np
import matplotlib.pyplot as plt

#f(x) = x^4 + 2x^3 - 9x^2 + 5

polynom1 = np.array([1,2,-9,-2,5])
x = np.linspace(-5,3.200)
y = np.polyval(polynom1,x)
plt.figure('Polynom')
plt.plot(x,y,label="$f(x) = x^4 + 2\cdot x^3 - 9\cdot x^2 + 5$")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()


# Nullstellen
Pol_roots = np.roots(polynom1)
print(Pol_roots)
plt.figure('Roots')
y_0 = np.zeros(Pol_roots.shape)
plt.plot(x,y,label="$f(x) = x^4 + 2\cdot x^3 - 9\cdot x^2 + 5$")
plt.plot(Pol_roots,y_0,'*',label="Roots")


plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()


# Ableitungen/Integration
plt.figure('Ableitung/Integration')
plt.plot(x,y,label="$f(x) = x^4 + 2\cdot x^3 - 9\cdot x^2 + 5$")
plt.plot(Pol_roots,y_0,'*',label="Roots")

poly_Abl = np.polyder(polynom1)
poly_Int = np.polyint(polynom1)

print(poly_Abl)
print(poly_Int)

plt.plot(x,np.polyval(poly_Abl,x), label="Ableitung")
plt.plot(x,np.polyval(poly_Int,x), label="Integration")


plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
