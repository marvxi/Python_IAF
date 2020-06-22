import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,500)
y_1 = np.sin(x**2)
y_2 = np.sin(x**2)*0.6

'''
plt.plot(x,y_1,'k->',label=r"$sin(x^2)$") # Latex code, einfügen von belibiegen Funktionen
plt.plot(x,y_2,'k-x',label=r"sin(x^2)*0.6") # Linie als striche anzeigen
plt.plot(x,y_2*0.2,'k-+',label=r"sin(x^2)*0.2") # Linie als striche und punkte anzeigen
'''
plt.plot(x,y_2*0.7,'k-3',linewidth=1,markevery=100,label=r"sin(x^2)*0.2") #markervery, jeder x wert wird gemarkert

markerListe=['.','o','>','d']

for i,mar in enumerate(markerListe):
    plt.plot(x,y_2+i,marker=mar,markevery=20,linewidth=0.5,label='$sind$+{}'.format(i))


plt.xlabel("x")
plt.ylabel("y")
plt.title("Sinus")
plt.grid()
plt.legend()
plt.show()
