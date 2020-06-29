import numpy as np
import matplotlib.pyplot as plt

#Printoptin
np.set_printoptions(suppress=True,precision=3)

class LGS_System:

    def __init__(self,A,l):
        self.A = A
        self.l = l

    def LGS_info(self,verbos=0):
        self.detA = np.linalg.det(self.A)
        self.conA = np.linalg.cond(self.A)
        try:
            self.I = np.dot(A,np.linalg.inv(A))
        except:
            self.I = None
        if verbos:
            print('--Eq. System Info--')
            print('System Matrix A: ')
            print(self.A)
            print('Lösungsvektor: ')
            print(self.l)
            print("Singularitätstest A*A^1")
            if self.I is not(None):
                print(self.I)
            else:
                print("Die Matrix A ist singulär")
            print(f'Determinate det(A): {self.detA:.3f}')
            print(f'Kondiitionszahl cond(A): {self.conA:.3f}')
        return([self.detA,self.conA,self.I])

    def LGS_solve(self):
        try:
            np.linalg.solve(self.A, self.b)
        except:
            print("Warnung, System nicht eindeutig lösbar. \n Nährungslösung wird berechnet")
            x = np.linalg.lstsq(self.A, self.l)[0]  # Annährung
        return x





#--------------------------------
#System 1 -----------------------
print("System 1")
A = np.array(([1,-2,1],[2,1,-1],[-1,-4,3]))
l = np.array([6,-3,14])

System1 = LGS_System(A,l)
System1.LGS_info(1)

x1 = np.linalg.solve(A,l)
print(f'Lösung für:\n {A}\n ist: {x1}')

#System 2 -----------------------
print("System 2")
A2 = np.array(([1,2,2],[2,3,1],[3,5,3]))
l2 = np.array([-2,1,-1])

#System 3 -----------------------
print("System 3")
A3 = np.array(([1,1,1],[3,3,3],[5,5,5]))
l3 = np.array([3,4,9])
System3 = LGS_System(A3,l3)
System3.LGS_solve()




# -----------------------------------------------
# define system for plot
A=A3
b=l3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# define space
res=11
x1 = np.linspace(-6,6,51)
x2 = np.linspace(-6,6,51)
xx, yy = np.meshgrid(x1, x2)
# -----------------------------------------------
# calculate surfaces zz-values
MyColors=['deepskyblue', 'lightgreen', 'salmon']
MyLabel=['Gl.1','Gl.2','Gl.3']
zz=np.zeros((b.shape[0],xx.shape[0],xx.shape[1]))
for i in range(len(b)):
	zz[i]=(-A[i,0]*xx -A[i,1]*yy +b[i]) / A[i,2]
	surf=ax.plot_surface(xx, yy, zz[i], alpha=0.3, color=MyColors[i], label=MyLabel[i])
	surf._facecolors2d=surf._facecolors3d
	surf._edgecolors2d=surf._edgecolors3d
print('---------------------------')
try:
	# calculate LGS solution
	x = np.linalg.solve(A,b)
except:
	# calculate nearest LGS solution
	x = np.linalg.lstsq(A,b)[0]
print(f'Lösung für x: {x}')
print(f'A*x={np.dot(A,x)} | b={b}')# A*x = b

ax.scatter(x[0], x[1], x[2], color='black')

sol_x=np.abs(x1 - x[0]).argmin()
sol_y=np.abs(x2 - x[1]).argmin()

lw=1.0
# line along y-axis
ax.plot(xx[sol_y], yy[sol_y], zz[0,sol_y],'--', color='royalblue', linewidth=lw)
ax.plot(xx[sol_y],yy[sol_y], zz[1,sol_y],'--', color='forestgreen', linewidth=lw)
ax.plot(xx[sol_y], yy[sol_y], zz[2,sol_y],'--', color='coral', linewidth=lw)

ax.plot(xx[:,sol_x],yy[:,sol_x],zz[0,:,sol_x],'--', color='royalblue', linewidth=lw)
ax.plot(xx[:,sol_x],yy[:,sol_x],zz[1,:,sol_x],'--', color='forestgreen', linewidth=lw)
ax.plot(xx[:,sol_x],yy[:,sol_x],zz[2,:,sol_x],'--', color='coral', linewidth=lw)
# -----------------------------------------------
plt.title('LGS LÃ¶sung')
plt.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()