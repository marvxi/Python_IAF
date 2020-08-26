import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

#Handle close
def handle_close(event):
    print('Close figure')
    quit()

# Schrittweite dx = dy = h
h = 0.2
# Material definition
D = 10.

# Zeitschritt
dt = h**2/(4*D)

# Plattengröße
higth = width = 10.

# Anzahl der Schritt im Raum
nx,ny = int(width/h),int(higth/h)

x = np.linspace(0,width,nx)
y = np.linspace(0, higth, ny)

X,Y = np.meshgrid(x,y)

# Zeitdauer in sek.
t = 2

# Anfangsbedingungen
Tcool, Thot = 10,150
u = np.zeros((nx,ny))
u0 = Thot * np.ones((nx,ny))

# Rand
x = np.linspace(0,width,nx)


u0[:,0] = -((4*Thot)/width**2)*x**2 + ((4*Thot)/width)*x
u0[:,nx-1] = Tcool

u0[0,:] = Tcool
u0[ny-1,:] = Tcool



u=u0.T

# Plots
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Temperatur')
ax.set_zlim3d(0.0,200.0)

wframe = None


for time in np.linspace(0,t,int(t/dt)):
    if wframe:
        ax.collections.remove(wframe)
        textvar.set_visible(False)
    for i in range(1,len(x) - 1): # beachte Gleichung !
        for j in range(1,len(y) - 1): #beachte Gleichung !

            u[i, j] = (1 - (4 * dt * D) / h ** 2) * u0[i, j] + (dt * D) / h ** 2 * (
                        u0[i, j - 1] + u0[i - 1, j] + u0[i + 1, j] + u0[i, j + 1])

    wframe = ax.plot_surface(X,Y,u,cmap=cm.jet)
    textvar = ax.text(10,12,200,f't={time:.4}')
    u0=u.copy()
    plt.pause(0.1)
    fig.canvas.mpl_connect('close_event',handle_close) # Close event
plt.show()