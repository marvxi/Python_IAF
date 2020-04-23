from math import sqrt

v0 = 5
g = 9.81
#yc = float(input('Höhe des Tennisballs yc = '))
yc = float(1)
t1=1./g*(-sqrt(-2*g*yc+v0*v0)+v0)
t2=1./g*(sqrt(-2*g*yc+v0*v0)+v0)
#print(y)
print('Der Ball ist auf der Höhe %9.2f m. after t1=%6.2f s' %(yc,t1))
print('and after t2 = %6.2f s'%(t2))
