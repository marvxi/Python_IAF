import numpy as np
import matplotlib.pyplot as plt

Tabelle = open(r'C:\Users\Marvi\OneDrive\03_Studium Unterlagen\10_Master\03_Semester\02_Python\02_UE\Federkennlinie.txt', 'r')
Tabelle.readline()

Weg = []
Kraft = []

for line in Tabelle:
    strings = line.split()
    Wege = float(strings[0])
    Krafts = float(strings[1])

    Weg.append(Wege)
    Kraft.append(Krafts)

Tabelle.close()

for i in range(0,6):
    print('%-10s %-10g' %(Weg[i],Kraft[i]))

apporx = np.polyfit(Weg,Kraft,deg=1)
apporx2 = np.polyfit(Weg,Kraft,deg=2)

print(f'Kraft bei 3.5cm: {np.polyval(apporx2,3.5):.3f} N')

plt.plot(Weg,np.polyval(apporx,Weg),'r--',label='Approximation Gerade')
plt.xlabel("Weg")
plt.ylabel("Approx.")
plt.legend()



plt.plot(Weg,np.polyval(apporx2,Weg),'b--',label='Approximation 2-Grades')
plt.legend()


plt.plot(Weg,Kraft,'s--',label="Original")
plt.legend()

plt.grid()
plt.show()





