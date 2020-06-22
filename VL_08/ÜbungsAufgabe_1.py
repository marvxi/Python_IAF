import numpy as np
import matplotlib.pyplot as plt

#f(x) = x^4 - x^3 - 4x^2 + 4x

polynom = np.array([4,-3,-2,1])
x = np.linspace(-5,5,200)
y = np.polyval(polynom,x)


plt.figure("Polynome + Alles andere")
plt.subplot(2,2,1)
plt.plot(x,y,label="$f(x) = x^4 - x^3 - 4x^2 + 4x$")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

# Funktionswerte
fWerte = [-4,-2,0,2,4]
for i in fWerte:
    print('Funktionswerte an den Stellen: {} sind: {}'.format(i,y[i]))

# Nullstellen
Pol_roots = np.roots(polynom)
yRoot = np.zeros(Pol_roots.shape)
print('Nullstellen des Polynoms: {}'.format(Pol_roots))
plt.subplot(2,2,2)
plt.plot(Pol_roots,yRoot,"*-",label="Nullstellen")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

#Ableitung/Integral

poly_Abl = np.polyder(polynom)
poly_Int = np.polyint(polynom)

plt.subplot(2,2,3)
plt.plot(x,np.polyval(poly_Abl,x), label="Ableitung")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

plt.subplot(2,2,4)
plt.plot(x,np.polyval(poly_Int,x), label="Integration")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()