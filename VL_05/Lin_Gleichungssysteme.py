import numpy as np
A = np.array([[1,2],[3,4]])
b = np.array([[5],[11]])
y = np.linalg.solve(A,b) #solve löst gleichungssystem
print(y)
