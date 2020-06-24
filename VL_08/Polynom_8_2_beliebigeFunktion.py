import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

def fitFunc(x, a, b):
    return np.exp((-0.5)*(x-a)**2/(2*b**2))

x = np.linspace(-10,10,200)
y = fitFunc(x,2,1)

#Daten erzeugen
sigma = 0.1
e = sigma * np.random.randn(y.shape[0])
S = e + y

#Datafitting
popt, pcov = op.curve_fit(fitFunc,x,S) # Muss eine funktion ohne Klammer übergeben bekommen
#popt optimale parameter, pcov kovarianz matrix (zeigt wie gut welcher parameter abgeschätzt ist)
print(f'parameter: {popt}') #Vgl mit fitFunc a und b, hier mit 2 und 1 angegeben
print(f'covariance: {pcov}') # Erste und zweite Diagonale gibt an wie gut der erste und zweite parameter abgeschätzt ist
print(popt[0]/2,popt[1]/1) #Abschätzung in % von 2 und 1 (a,b)
#Plot
#plt.plot(x,y,"--",label="fitFunc")
plt.plot(x,S,"+",label="Signal")
plt.plot(x,fitFunc(x,popt[0],popt[1]),"*",label="FitFunction") #popt[0] a popt[1] b

plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()