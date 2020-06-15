import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,51) #0-10 in 0.2 Schritten

def Polynom(x,a=2,b=-10,c=4):
    y = []
    for i in range(len(x)):
        y.append(a*x[i]**2+b*x[i]+c) #nur append möglich da Liste leer
    return y

y = Polynom(x)

def polyDiff(x,y):
    diffFx =[]
    print('länge x', len(x))
    print("länge y",len(y))
    for i in range(1,len(y)-1): #Achte auf out of range
        diffFx.append((y[i+1] - y[i-1])/(2*(x[i+1]-x[i])))
    return diffFx

print(polyDiff(x,y))

def plot(x,y,polyDiff):
    plt.plot(x,y,label="y")
    plt.legend()
    plt.grid()
    #print(x)   # Erste und Letzte Eintrag muss gelöscht werden, da bei diff nicht betrachtet
    x = x[1:-1]
    #print(x)
    plt.plot(x,polyDiff,label="y'")
    plt.show()
plot(x,y,polyDiff(x,y))