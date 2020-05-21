import numpy as np

f = lambda m, n: n+10*m
A = np.fromfunction(f,(6,6),dtype=int)
print(A)
print(A[:,1]) #Alle Zeile aber nur die 1 spalte in Zeilenform
print(A[:3,:3])
print(A[3:,:3])