import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,200)
y = np.polyval([2,0,0],x)

#Randomfunktion/ Rauschen / e = Fehler
mu = 0
sigma = 1 # Gibt die "Streuung" an bzw. den Bereich in dem die Daten liegen
e = sigma * np.random.randn(y.shape[0]) #normalverteilte
S = y + e

# Data fitting
p = np.polyfit(x,S,deg=2)#deg gibt Grad des Polynoms an
p_info = np.polyfit(x,S,deg=2,full=True) # full=True zeigt die gesamten Inforamtionen an
print(p_info[1])


plt.plot(x,np.polyval(p,x),label="Data fit")
plt.plot(x,y,'--',label='reale Funktion')
plt.plot(x,S,'+',label="Signal")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()