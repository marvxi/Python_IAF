import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

N = 50
#Achse erstellen
x = np.linspace(-np.pi,np.pi,N) #xAchse
y = x                           #yAchse

# Raster erstellen
X,Y = np.meshgrid(x,y)

#Funktion
Z=np.exp(-(X**2+Y**2))

# Fenster erstellen
fig = plt.figure()

ax = fig.add_subplot(projection='3d') # Sagt matplotlib das man einen 3D Plot will
surf = ax.plot_surface(X,Y,Z,cmap=cm.jet,label='3D Gauss') # cmap ist eine Farbenmap

#Stoplerfalle bzgl. den labels!!
surf.facecolors2d = surf._facecolors3d
surf.edgedcolor2d = surf._edgecolors3d

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()



'''
print(f'x-ist von Typ{type(X)}')
print(f'x hat die Größe: {x.shape}')
print(X)
print("----------------------------")
print(f'y-ist von Typ{type(Y)}')
print(f'y hat die Größe: {x.shape}')
print(Y)
'''



