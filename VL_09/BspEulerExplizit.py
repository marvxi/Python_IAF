import numpy as np
import matplotlib.pyplot as plt

t1 = np.arange(0,5,0.01)
#Analytische Lösung
y1 = 2.5*t1**2

plt.figure()
plt.xlabel("t")
plt.ylabel("y")
plt.plot(t1,y1,label="Analytische Lösung")



# Numerische Lösung explizite Euler

h = 0.1
t2 = np.arange(0,5,h)
y2 = np.zeros(len(t2))

for i in range(1, len(t2)):
    y2[i] = y2[i-1] + h*5*t2[i-1]

plt.plot(t2,y2,'--',linewidth=2,label="Numerische Lösung")
plt.legend()
plt.grid()
plt.show()

