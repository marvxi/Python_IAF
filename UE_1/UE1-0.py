import numpy as np

x = input('x=')

if x.isalpha():
    if x=='pi' or x=='Pi' or x=='PI':
        x=np.pi
    if x=='e' or x=='E':
        x=np.e
    else:
        print('ERROR: invalid input')
        exit(0)
else:
    x = float(x)
print(x)