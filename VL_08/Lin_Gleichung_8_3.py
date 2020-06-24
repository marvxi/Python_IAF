import numpy as np
import matplotlib.pyplot as plt

#Printoptin
np.set_printoptions(suppress=True,precision=3)
#--------------------------------
#System 1 -----------------------
print("System 1")
A = np.array(([1,-2,1],[2,1,-1],[-1,-4,3]))
l = np.array([6,-3,14])
print(f'Determinate: det(A)={np.linalg.det(A)}')
print('Singualirtätstest A*A^-1:')
print(np.dot(A,np.linalg.inv(A)))
print(f'Konditionszahl: cond(A) = {np.linalg.cond(A):.3f}')



#System 2 -----------------------
print("System 2")
A = np.array(([1,2,2],[2,3,1],[3,5,3]))
l = np.array([-2,1,-1])
print(f'Determinate: det(A)={np.linalg.det(A)}')
print('Singualirtätstest A*A^-1:')
print(np.dot(A,np.linalg.inv(A)))
print(f'Konditionszahl: cond(A) = {np.linalg.cond(A):.3f}')



#System 3 -----------------------
print("System 3")
A = np.array(([1,1,1],[3,3,3],[5,5,5]))
l = np.array([3,4,9])
print(f'Determinate: det(A)={np.linalg.det(A)}')
print('Singualirtätstest A*A^-1:')
try:
    print(np.dot(A,np.linalg.inv(A))) # Kann nicht invertiert werden da nicht singulär
except:
    print("Matrix kann nicht invertiert werden")
print(f'Konditionszahl: cond(A) = {np.linalg.cond(A):.3f}')

