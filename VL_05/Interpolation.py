import numpy as np
from scipy.interpolate import interp1d
import pylab

x_max = 2*np.pi
x = np.linspace(0,x_max,8)
y = np.sin(x)

x2 = np.linspace(0,x_max,80)


#--Interpolation
f_lin = interp1d(x,y) #Interpolation linear
#--exakt
f_ex = np.sin(x2)
#--Differenz
fx = f_lin(x2)
f_diff = f_ex - fx
maxdiff = max(f_diff)
print('Maximale Differenz: ', maxdiff)


pylab.plot(x2,f_lin(x2)) # Achtung neues x2 erstellen für mehr Stellen, da glatter!
pylab.plot(x,y,'o',label='data points')
pylab.plot(x2,f_ex)
pylab.show()
pylab.plot()

# Die veränderung der Punkte von 8 auf 80 führt dazu das die Differenz zu null wird.