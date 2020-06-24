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





#--------------------------------
#System 1 -----------------------
print("System 1")
A = np.array(([1,-2,1],[2,1,-1],[-1,-4,3]))
l = np.array([6,-3,14])

System1 = LGS_System(A,l)
System1.LGS_info(1)

#System 2 -----------------------
print("System 2")
A = np.array(([1,2,2],[2,3,1],[3,5,3]))
l = np.array([-2,1,-1])

#System 3 -----------------------
print("System 3")
A = np.array(([1,1,1],[3,3,3],[5,5,5]))
l = np.array([3,4,9])