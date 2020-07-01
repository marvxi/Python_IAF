import numpy as np
import matplotlib.pyplot as plt

for x in reversed(range(1,10)):
    plt.figure(1)
    daten = np.random.normal(5,0.1*x,10000)
    n,bins,patches = plt.hist(daten,50)

plt.show()



