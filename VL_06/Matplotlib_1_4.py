import matplotlib.pyplot as plt
import numpy as np

#------------------------------------
#Daten
#------------------------------------

x = np.linspace(0,2*np.pi,500)
y_1 = np.sin(x)
y_2 = np.cos(x)
y_3 = np.tan(x)
y_4 = np.tanh(x)

fig = plt.figure("Meine Subplots")
gs = fig.add_gridspec(3,2) #3 Zeilen, 2 Spalten

# 1 Achse
ax1 = fig.add_subplot(gs[0,0]) #Zuweisung
ax1.plot(x,y_1)
# 2 Achse
ax2 = fig.add_subplot(gs[0,1]) #Zuweisung
ax2.plot(x,y_2)
# 3 Achse
ax3 = fig.add_subplot(gs[1,0]) #Zuweisung
ax3.plot(x,y_3)
# 4 Achse
ax4 = fig.add_subplot(gs[1,1]) #Zuweisung
ax4.plot(x,y_4)
# 5 Achse
ax5 = fig.add_subplot(gs[2,:]) #Zuweisung, der doppelpunkt sag das man die ganze Zeile verwendet
ax5.set_ylim([-5,5]) # Bereich der geplottet werden soll
ax5.plot(x,y_1)
ax5.plot(x,y_2)
ax5.plot(x,y_3)
ax5.plot(x,y_4)

plt.show()