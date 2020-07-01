import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,100,1) # 1-100 in einerschritte auch float mögliche !!
#print(x)
num_y = 20
y = np.sin(x/5)*num_y+num_y # Warum num_y *+??
#print(y)
A = np.zeros([len(x),2*num_y])
print(A.shape)
for i in range(len(x)):
    position = int(y[i])
    A[i,position] = 1
plt.matshow(A.transpose())
plt.show()



'''
f = np.empty([2,int(2*np.pi/0.1)])
x = 0
count = 0
while x <= 2*np.pi:

    f[0][count-1] = np.sin(x)
    f[1][count-1] = x
    count += 1
    x+=0.1

plt.matshow(f.transpose(),interpolation="none")
plt.show()

'''