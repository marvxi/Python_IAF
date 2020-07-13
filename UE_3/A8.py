import numpy as np
import matplotlib.pyplot as plt

umdrehung = []
leistung = []
for i in range(12):
    if i == 0:
        umdrehung.append(1000.00)
        leistung.append(4.529)
    else:

        umdrehung.append(umdrehung[i-1] + np.random.uniform(350,500))
        leistung.append(leistung[i-1] + np.random.uniform(3,8))

polynom1 = np.array([-1.3500e-13,2.943e-9,-2.5004e-5, 0.0779, 59.9732])
n1 = np.linspace(1000,6000,100)
drehmoment = np.polyval(polynom1,n1)
print(f" Drehmoment: {drehmoment}\n, Leistung: {leistung}\n, Umdrehung: {umdrehung} ")

#Plot auf Achsen links und rechts
fig, ax1 = plt.subplots() #erzeugt neue figure mit axe ax1

#linke y-achse
pl1=ax1.plot(n1,np.polyval(polynom1,n1),label='Drehmoment')

ax1.set_xlim([0,7000])
ax1.set_ylim([0,160])

ax1.set_xlabel('Drehzahl [1/min]')
ax1.set_ylabel('Drehmoment [Nm]', color = 'blue')

# rechte y achse

ax2 = ax1.twinx()
pl2=ax2.plot(umdrehung,leistung,'g.-',label='Leistung')
ax2.set_ylim([0,60])
ax2.set_ylabel('Leistung [kW]', color='green')
# Plot-Beschriftung
plt.title('Motorkennlinie Golf 3 AAM')
ax1.legend(loc=3)
ax2.legend(loc=4)
plt.grid()
plt.show()
