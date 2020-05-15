import numpy as np

x = np.pi

y=4.3
#old school
#print('x:%6.4f' %(x))
#print('x:%6.9f' %(x))

# format()
#print('x:{6.1}'.format(3)) #??? warum gehts nicht ?

#f-strings
#print(f'x{x:.5}')

# Rundungsfehler
#x=7/3-4/3-1
#print(f'x={x:.50f}')

# Nach Lösung
print(f'x={x:.6}') #vor dem . werden Zeichen reserviert