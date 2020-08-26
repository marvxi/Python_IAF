import numpy as np
import matplotlib.pyplot as plt

Tabelle = open(r'C:\Users\Marvi\OneDrive\03_Studium Unterlagen\10_Master\03_Semester\02_Python\02_UE\Beschleunigungsverlauf.txt','r')
Tabelle.readline()


Zeit = []
Weg = []

for line in Tabelle:
    strings = line.split()
    Zeiten = float(strings[0])
    Wege = float(strings[1])

    Zeit.append(Zeiten)
    Weg.append(Wege)

#Beschleunigung
Weg1 = Weg[0:6]
Zeit1 = Zeit[0:6]

#Bremse
Weg2 = Weg[5:-1]
Zeit2 = Zeit[5:-1]


plt.subplot(3,1,1)
plt.plot(Zeit1,Weg1,'b',label="Beschleunigung")
plt.plot(Zeit2,Weg2,'r',label='Bremsvorgang')
plt.xlabel("Zeit t [s]")
plt.ylabel("Weg x [m]")
plt.legend()
plt.grid()
#plt.show()

# Poly für zwischenwerte
PolyBeschleunigung = np.polyfit(Zeit1,Weg1,deg=2)
PolyBremse = np.polyfit(Zeit2,Weg2,deg=2)

print(f'Das Fahrzeug hat nach 5 sek. die Strecke: {np.polyval(PolyBeschleunigung,5):.3f} Meter und nach 35 sek. die Strecke:'
      f'{np.polyval(PolyBremse,35):.3f} Meter zurück gelegt.')

# Ableitung für Geschwindigkeit
GeschwindigkeitBeschl = np.polyder(PolyBeschleunigung)
GeschwindigkeitBremse = np.polyder(PolyBremse)

# Interpoliere
GeschwindigkeitBeschlP = np.polyval(GeschwindigkeitBeschl,Zeit1)
GeschwindigkeitBremseP = np.polyval(GeschwindigkeitBremse,Zeit2)

plt.subplot(3,1,2)
plt.plot(Zeit1,GeschwindigkeitBeschlP,'b--',label="Beschleunigung")
plt.plot(Zeit2,GeschwindigkeitBremseP,'r--',label="Bremsenvorgang")
plt.xlabel("Zeit t [s]")
plt.ylabel("Geschwindigkeit")
plt.grid()
plt.legend()
#plt.show()

# Ableitung für Beschleunigung
#BeschleunigungBeschl = np.polyder(GeschwindigkeitBeschl)
#BeschleunigungBremse = np.polyder(GeschwindigkeitBremse)
#
##Interpoliere
#BeschleunigungBeschl = np.polyval(BeschleunigungBeschl,Zeit1)
#BeschleunigungBremse = np.polyval(BeschleunigungBremse,Zeit2)



plt.subplot(3,1,3)
plt.plot(Zeit1,np.polyval(np.polyder(GeschwindigkeitBeschl),Zeit1),'b--',label="Beschleunigung")
plt.plot(Zeit2,np.polyval(np.polyder(GeschwindigkeitBremse),Zeit2),'r--',label="Bremsvorgang")
plt.xlabel("Zeit t [s]")
plt.ylabel("Beschleunigung")
plt.grid()
plt.legend()
plt.show()