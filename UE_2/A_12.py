import matplotlib.pyplot as plt
import numpy as np

def plotting(b,c,d,a1=False,a2=False):
    a = np.arange(b[0],b[1])
    c = a**2+np.sin(a*c)+np.exp(a)
    if a1==True:
        plt.figure(1)
        plt.plot(a,c)
        plt.title('Ein wundervolles Programm')
        plt.xlabel('Zeit')
        plt.ylabel('Aktienkurs')
        plt.show()

plotting([0,5],0,0,True)

def plottinOptim(Bereich,dPlot=False):
     x = np.arange(Bereich[0],Bereich[1])
     y = x**2
     if dPlot == True:
         plt.figure(1)
         plt.plot(x, y)
         plt.title('Ein wundervolles Programm')
         plt.xlabel('Zeit')
         plt.ylabel('Aktienkurs')
         plt.show()
plottinOptim([0,5],True)
