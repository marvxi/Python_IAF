import sys

v0 = float(sys.argv[1])
t = float(sys.argv[2])
g = 9.81
y = v0*t-0.5*g*t**2
print('At t=%9.1f s, the heigt of the ball is %9.2f m.' %(t,y))