import numpy as np


#data = [21.8,18.1,19,23,26,17.8]
data = open('data.txt','r') # r = lesezugriff

mean = 0
n = 0
while True:
    line = data.readline()
    if not line:
        break
    mean+=float(line)
    n+=1
print(np.average(data)) # Hier noch mean eintragen
infile.close()