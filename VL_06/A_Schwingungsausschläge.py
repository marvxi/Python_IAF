import matplotlib.pyplot as plt
import numpy as np

#Const
X = 5
D = 0.1
t = np.linspace(0,1,200)

Tau = 5*2*np.pi*t

y = lambda x:X*np.exp(-D*Tau)

plt.plot(t,y(Tau),label="Funktion") #Wichtig bei der lambda Funktion den x oder wat ever wert eingeben!


plt.xlabel("Zeit t") #Mindesanforderung für Plot!!! Wichtig
plt.ylabel("Ausschläge")
plt.legend()
plt.grid()
plt.show()