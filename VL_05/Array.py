import numpy as np

r = [x for x in range(1,6)]
r = np.array(r)

#print(r.shape) # in n Richtung
#print(r.ndim) # in m richtung
#print(r)

#-----
ar = np.array([[1,1],[2,2]])
ar2 = np.array([[3,3],[4,4]])
vek = np.array([2,2])
vek2 = np.array([3,3])

#print(ar.shape)
#print(ar.ndim)
#print(ar.diagonal())
#print(ar)
#print(ar.transpose())

#print(ar + ar2)# addition
print(ar)
print(vek)
print('Skalarprodukt: ',np.dot(vek2,vek))

#Kreuzprodukt

arkreu = np.array([1,2,3])
arkreu2 = np.array([2,3,4])
print(np.cross(arkreu,arkreu2))

#----Einfache Array-Operatoren

matrix = np.array([[1,1,1],[2,2,2],[3,3,3]])

print(arkreu2[1:]) # von.. bis
print(matrix)
print(matrix[:,2]) # alle Zeilen von Zeilen von Spalte 1
print(matrix[0:2,0:3])# Abschnittsweise der Erste ist Zeilen und zweite welche Spalten

print(np.linspace(0,100,20)) # 20 Werte zwischen Null und 100
print(np.logspace(1,5,4,base=2)) #4werte zwischen 1 und 5 zur basis 2
print(np.identity(3)) #Einheitsmatrix
print(np.diag(np.ones(5)))
