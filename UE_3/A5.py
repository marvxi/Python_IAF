import numpy as np
import matplotlib.pyplot as plt

def func(A,n):
    x = []
    y = []
    for i in range(len(A[n])):
        x.append(i)
        y.append(A[n][i-1])

    plt.plot(x,y,label="Matrixzeile")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()
matrix = np.array(([-1,2,-1,2],[2,2,2,2,2],[1,2,6,5]))
#func(matrix,0)

def funcLsg(A,n):
    plt.figure()
    plt.plot(A[n,:]) # Gute Variante kurzer code !
    plt.title('A5')
matrixx = np.random.rand(20,20)
funcLsg(matrixx,10)
plt.show()

